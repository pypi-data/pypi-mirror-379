import asyncio
import json
import re
import traceback
from dataclasses import dataclass, field
from itertools import combinations
from pathlib import Path
from typing import Optional

import numpy as np
import typer
from langdetect import detect, DetectorFactory
from rich import print
from tqdm import tqdm

from dygest import llms, ner_utils, output_utils, prompts, json_schemas, utils
from dygest.ner_utils import NERlanguages
from dygest.output_utils import ExportFormats
from dygest.translations import LANGUAGES


@dataclass
class DygestBaseParams:
    filepath: str
    output_dir: str = "./output"
    light_model: Optional[str] = None
    expert_model: Optional[str] = None
    embedding_model: Optional[str] = None
    temperature: float = 0.1
    sleep: float = 0
    chunk_size: int = 1000
    add_toc: bool = False
    add_summaries: bool = False
    add_keywords: bool = False
    add_ner: bool = False
    sim_threshold: float = 0.8
    provided_language: NERlanguages = NERlanguages.AUTO
    precise: bool = False
    verbose: bool = False
    export_metadata: bool = False
    export_format: ExportFormats = ExportFormats.HTML
    html_template_path: Path = None


@dataclass
class DygestProcessor(DygestBaseParams):
    ner_tagger: Optional[object] = field(default=None, init=False)
    text: Optional[str] = field(default=None, init=False)
    chunks: Optional[dict] = field(default=None, init=False)
    sentence_offsets: Optional[str] = field(default=None, init=False)
    toc: Optional[list] = field(default=None, init=False)
    summaries: Optional[str] = field(default=None, init=False)
    keywords: Optional[list] = field(default=None, init=False)
    entities: Optional[list] = field(default=None, init=False)
    token_count: Optional[int] = field(default=None, init=False)
    language_ISO: NERlanguages = field(default=None, init=False)
    language_string: str = field(default=None, init=False)
    files_to_process: list[Path] = field(default_factory=list)
    ner_model_cache: dict[str, object] | None = None
    current_ner_model_key: Optional[str] = field(default=None, init=False)
    file_ner_models: dict[Path, object] = field(
        default_factory=dict, init=False
    )
    current_input_file: Optional[Path] = field(default=None, init=False)

    def __post_init__(self):
        self.output_dir = Path(self.output_dir)
        if not self.output_dir.exists():
            self.output_dir.mkdir(parents=True)
            if self.verbose:
                print(f"... Created output directory at {self.output_dir}")

        if self.ner_model_cache is None:
            self.ner_model_cache = {}

        # Cache baseline parameters so we can safely adjust them per file.
        self._base_light_model = self.light_model
        self._base_expert_model = self.expert_model
        self._base_chunk_size = self.chunk_size
        self._base_add_toc = self.add_toc
        self._base_add_summaries = self.add_summaries
        self._base_add_keywords = self.add_keywords
        self._base_provided_language = self.provided_language
        self._base_sim_threshold = self.sim_threshold
        self._base_export_format = self.export_format

    def run_language_detection(self) -> str:
        """
        Get language of text to set the correct NER model.

        Returns:
            str: An ISO 639-1 language code ('en', 'de', 'es' ...)
        """
        provided_lang = self.provided_language
        if isinstance(provided_lang, NERlanguages):
            provided_lang = provided_lang.value

        if provided_lang == 'auto':
            DetectorFactory.seed = 0
            language_ISO = detect(self.text[:500])
            print(f"... Detected language '{language_ISO}'")
        else:
            language_ISO = provided_lang
        return language_ISO

    def run_ner(self) -> list[str] | None:
        """
        Run Named Entity Recognition with flair framework on the text.
        """
        if not self.language_ISO:
            return []

        tagger = self._get_or_load_ner_model(self.language_ISO)

        # Run Named Entity Recognition (NER)
        entities = ner_utils.get_flair_entities(self.text, tagger)
        all_entities = ner_utils.update_entity_positions(entities, self.text)

        if self.verbose:
            print("... ENTITIES FOR DOC:")
            utils.print_entities(all_entities)

        return all_entities

    async def create_toc_async(self) -> dict:
        """
        Async version of create_toc.
        Create a Table of Contents (TOC) for the provided file.
        """
        def is_valid_location(location: str) -> bool:
            """
            Validate if a topic location follows this sentence id ("s_id")
            structure: "S362"
            """
            return bool(re.fullmatch(r'S[1-9]\d*$', location))

        def fix_wrong_location(location: str) -> str:
            """
            Try to fix a malformed topic location structure.

            Transforms strings like:
            - "S<019>" to "S19"
            - "S09" to "S9"
            """
            if re.fullmatch(r'S<\d+>', location):
                intermediate = re.sub(r'[<>]', '', location)
                fixed = re.sub(r'S0+', 'S', intermediate)
                return None if fixed == 'S' else fixed
            elif re.fullmatch(r'S0+\d+', location):
                fixed = re.sub(r'S0+', 'S', location)
                return None if fixed == 'S' else fixed
            return None

        def align_toc_part(toc_part: list[dict], chunk: dict) -> list[dict]:
            """
            Align the topic locations (e.g. "S7") to match them with the
            correct chunk sentence IDs. The goal is to ensure the 'location'
            is one of the actual global sentence IDs present in the chunk.
            """
            # Check for a structured json output ('topics' key is present)
            if 'topics' in toc_part:
                toc_part = toc_part['topics']

            chunk_s_ids_global = chunk['s_ids']  # list[str] ['S47', 'S48' ...]
            if not chunk_s_ids_global:
                if self.verbose:
                    msg = (
                        "... Warning: Empty chunk_s_ids_global "
                        "in align_toc_part."
                    )
                    print(msg)
                return []

            # Convert global sentence IDs of chunk to numbers for comparison
            try:
                chunk_s_nums_global = (
                    [int(sid[1:]) for sid in chunk_s_ids_global]
                )
            except ValueError as e:
                if self.verbose:
                    msg = (
                        "... Warning: Could not parse sentence numbers from "
                        f"chunk_s_ids_global: {chunk_s_ids_global}. Error: {e}"
                    )
                    print(msg)
                return toc_part  # Return original if parsing fails

            default_location = chunk_s_ids_global[0]

            aligned_toc_part = []
            for topic in toc_part:
                original_llm_location = topic.get('location')
                current_location_str = None

                # Validate and fix the LLM's proposed location
                if (
                    original_llm_location
                    and is_valid_location(original_llm_location)
                ):
                    current_location_str = original_llm_location
                elif original_llm_location:
                    fixed_loc = fix_wrong_location(original_llm_location)
                    if fixed_loc and is_valid_location(fixed_loc):
                        current_location_str = fixed_loc

                # Default to start of chunk
                final_location_str = default_location

                if current_location_str:
                    # Case 1: LLM's location is a valid global ID
                    # within this chunk's sentences
                    if current_location_str in chunk_s_ids_global:
                        final_location_str = current_location_str
                    else:
                        # Case 2: LLM's location is not in this chunk's s_ids
                        # Try to find the closest valid s_id from this chunk
                        try:
                            llm_loc_num = int(current_location_str[1:])

                            # Ensure list is not empty
                            if chunk_s_nums_global:
                                closest_s_num = min(
                                    chunk_s_nums_global,
                                    key=lambda x: abs(x - llm_loc_num)
                                )
                                final_location_str = f"S{closest_s_num}"

                        except ValueError:
                            # Stick to default_location
                            if self.verbose:
                                msg = (
                                    "... Warning: Could not parse number from "
                                    f"LLM location '{current_location_str}'. "
                                    f"Using default '{default_location}'."
                                )
                                print(msg)
                else:
                    # No valid or fixable location string from LLM
                    # Stick to default_location
                    if self.verbose and original_llm_location:
                        msg = (
                            "... Warning: "
                            f"LLM location '{original_llm_location}' was "
                            "invalid and unfixable. Using default "
                            f"'{default_location}'."
                        )
                        print(msg)

                topic['location'] = final_location_str
                aligned_toc_part.append(topic)

            return aligned_toc_part

        # TOC processing
        print(f'... Creating TOC with {self.light_model}')

        complete_toc_parts = []
        for chunk_key, chunk_data in tqdm(self.chunks.items()):
            result = await llms.call_allm(
                prompt=prompts.build_prompt(
                    template=prompts.GET_TOPICS,
                    first_sentence=chunk_data['s_ids'][0],
                    last_sentence=chunk_data['s_ids'][-1],
                    language=self.language_string,
                    chunk=chunk_data['text']
                    ),
                model=self.light_model,
                output_format='json_schema',
                json_schema=json_schemas.GET_TOPICS_JSON,
                temperature=self.temperature,
                sleep_time=self.sleep
            )

            # Validate for correct JSON format
            toc_part = utils.validate_LLM_result(result, self.verbose)

            # Re-align topic locations
            toc_part = align_toc_part(toc_part, chunk_data)

            # Append toc_part
            complete_toc_parts.extend(toc_part)

            if self.verbose:
                print(f"... TOC PART FOR {chunk_key.upper()}:")
                utils.print_toc_topics(toc_part)

        # Post-Processing: Remove similar summaries
        print('... Removing similar TOC entries')
        sp = SummaryProcessor(
            summaries=complete_toc_parts,
            embedding_model=self.embedding_model,
            key='topic',
            threshold=self.sim_threshold,
            verbose=self.verbose
        )
        filtered_toc_parts = await sp.get_filtered_summaries()

        # Post-Processing: Create TOC
        print(f'... Compiling TOC with {self.expert_model}')
        toc = await llms.call_allm(
            prompt=prompts.build_prompt(
                template=prompts.CREATE_TOC,
                toc_parts=str(filtered_toc_parts),
                language=self.language_string
                ),
            model=self.expert_model,
            output_format='json_schema',
            json_schema=json_schemas.CREATE_TOC_JSON,
            temperature=self.temperature,
            sleep_time=self.sleep
            )

        # Validate LLM response
        toc = utils.validate_LLM_result(toc)
        final_toc = utils.validate_toc(toc)

        return final_toc

    async def create_summaries_and_keywords_async(self) -> tuple[dict, dict]:
        """
        Async version of create_summaries_and_keywords.
        Create summaries and keywords in one go.
        """
        print(f'... Creating summary and keywords with {self.light_model}')

        summaries = []
        keywords = []
        for chunk_key, chunk_data in tqdm(self.chunks.items()):
            result = await llms.call_allm(
                prompt=prompts.build_prompt(
                    template=prompts.CREATE_SUMMARY_AND_KEYWORDS,
                    text_chunk=chunk_data['text'],
                    language=self.language_string
                    ),
                model=self.light_model,
                output_format='json_schema',
                json_schema=json_schemas.CREATE_TOC_JSON,
                temperature=self.temperature,
                sleep_time=self.sleep
            )

            # Validate
            validated_result = utils.validate_LLM_result(result)

            # Append
            summaries.append(validated_result['summary'])
            keywords.extend(validated_result['keywords'])

            if self.verbose:
                print(f"... SUMMARY FOR {chunk_key.upper()}:")
                utils.print_summaries(validated_result['summary'])
                print("...")
                print(f"... KEYWORDS FOR {chunk_key.upper()}:")
                utils.print_summaries(validated_result['keywords'])

        print(f'... Harmonizing summaries with {self.expert_model}')
        final_summary = await llms.call_allm(
            prompt=prompts.build_prompt(
                template=prompts.COMBINE_SUMMARIES,
                summaries='\n'.join(summaries),
                language=self.language_string
                ),
            model=self.expert_model,
            temperature=self.temperature,
            sleep_time=self.sleep
        )

        # Create a unique set of keywords
        keywords_for_doc = self.clean_generated_keywords(keywords)

        # Remove similar keywords
        print('... Removing similar keywords')
        sp = SummaryProcessor(
            keywords=keywords_for_doc,
            embedding_model=self.embedding_model,
            key='topic',
            threshold=self.sim_threshold,
            verbose=self.verbose
            )
        filtered_keywords = await sp.get_filtered_keywords()

        return final_summary, filtered_keywords

    async def create_summaries_async(self) -> str:
        """
        Async version of create_summaries.
        Create summaries.
        """
        print(f'... Creating summary with {self.light_model}')

        summaries = []
        for chunk_key, chunk_data in tqdm(self.chunks.items()):
            summary = await llms.call_allm(
                prompt=prompts.build_prompt(
                    template=prompts.CREATE_SUMMARY,
                    text_chunk=chunk_data['text'],
                    language=self.language_string
                    ),
                model=self.light_model,
                temperature=self.temperature,
                sleep_time=self.sleep
            )
            summaries.append(summary)

            if self.verbose:
                print(f"... SUMMARY FOR {chunk_key.upper()}:")
                utils.print_summaries(summary)

        print(f'... Harmonizing summaries with {self.expert_model}')
        final_summary = await llms.call_allm(
            prompt=prompts.build_prompt(
                template=prompts.COMBINE_SUMMARIES,
                summaries='\n'.join(summaries),
                language=self.language_string
                ),
            model=self.expert_model,
            temperature=self.temperature,
            sleep_time=self.sleep
        )

        return final_summary

    async def generate_keywords_async(self):
        """
        Async version of generate_keywords.
        Generate keywords for the input text.
        """
        print(f'... Generating keywords with {self.light_model}')

        keywords_for_doc = []
        for chunk_key, chunk_data in tqdm(self.chunks.items()):
            keywords_for_chunk = await llms.call_allm(
                prompt=prompts.build_prompt(
                    template=prompts.CREATE_KEYWORDS,
                    text_chunk=chunk_data['text'],
                    language=self.language_string
                    ),
                model=self.light_model,
                temperature=self.temperature,
                sleep_time=self.sleep
            )
            keywords_for_doc.extend(keywords_for_chunk.split(','))

            if self.verbose:
                print(f"... KEYWORDS FOR CHUNK {chunk_key.upper()}:")
                utils.print_summaries(keywords_for_chunk)

        # Create a unique set of keywords
        keywords_for_doc = self.clean_generated_keywords(keywords_for_doc)

        # Remove similar keywords
        print('... Removing similar keywords')
        sp = SummaryProcessor(
            keywords=keywords_for_doc,
            embedding_model=self.embedding_model,
            key='topic',
            threshold=self.sim_threshold,
            verbose=self.verbose
            )
        filtered_keywords = await sp.get_filtered_keywords()

        return filtered_keywords

    def clean_generated_keywords(
        self,
        keywords_for_doc: str | list
    ) -> list[str]:
        """
        Return a unique list of keywords from LLM generated keyword list.
        """
        clean_keywords = set()

        for keyword in keywords_for_doc:
            keyword = utils.replace_underscores_with_whitespace(keyword)
            clean_keywords.add(keyword)

        return clean_keywords

    def _reset_base_params(self):
        """
        Restore parameters that may be temporarily overridden per file.
        """
        self.light_model = self._base_light_model
        self.expert_model = self._base_expert_model
        self.chunk_size = self._base_chunk_size
        self.add_toc = self._base_add_toc
        self.add_summaries = self._base_add_summaries
        self.add_keywords = self._base_add_keywords
        self.provided_language = self._base_provided_language
        self.sim_threshold = self._base_sim_threshold
        self.export_format = self._base_export_format

    def _reset_processing_vals(self):
        """
        Reset processing values for each file.
        """
        self.text = None
        self.chunks = None
        self.toc = None
        self.summaries = None
        self.keywords = None
        self.entities = None
        self.token_count = None
        self.language_ISO = None
        self.language_string = None
        self.sentence_offsets = None
        self.current_ner_model_key = None

    def _ner_cache_key(self, language: str) -> str:
        mode = 'precise' if self.precise else 'fast'
        return f"{language.lower()}::{mode}"

    def _get_or_load_ner_model(self, language: str):
        cache_key = self._ner_cache_key(language)
        if cache_key not in self.ner_model_cache:
            self.ner_model_cache[cache_key] = ner_utils.load_tagger(
                language=language,
                precise=self.precise
            )
            if self.verbose:
                print(f"... Cached NER model for '{cache_key}'")

        self.ner_tagger = self.ner_model_cache[cache_key]
        self.current_ner_model_key = cache_key
        if self.current_input_file is not None:
            self.file_ner_models[self.current_input_file] = self.ner_tagger

        return self.ner_tagger

    def _prepare_from_json(self, file: Path) -> bool:
        """
        Load a Dygest JSON export into the processor state.
        """
        self._reset_processing_vals()

        try:
            with open(file, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
        except json.JSONDecodeError as err:
            print(f"[purple]... Error: Invalid JSON file: {err}")
            return False
        except Exception as err:
            print(f"[purple]... Error processing JSON file: {err}")
            return False

        if not utils.validate_json_input(json_data):
            msg = (
                "... Error: The provided JSON does not follow the dygest "
                "JSON format."
            )
            typer.secho(msg, fg=typer.colors.RED)
            return False

        self.light_model = json_data['light_model']
        self.expert_model = json_data['expert_model']
        self.chunk_size = json_data['chunk_size']
        self.add_toc = 'toc' in json_data
        self.add_summaries = 'summary' in json_data
        self.add_keywords = 'keywords' in json_data
        self.provided_language = json_data['language']
        self.filename = json_data['filename']
        self.output_filepath = Path(json_data['output_filepath'])
        self.text = '\n'.join(
            chunk['text'] for chunk in json_data['chunks'].values()
        )
        self.chunks = json_data['chunks']
        self.token_count = json_data['token_count']
        self.language_ISO = json_data['language']
        language_str = LANGUAGES.get(json_data['language'])
        self.language_string = (
            language_str.title() if language_str else json_data['language']
        )
        self.sentence_offsets = json_data['sentence_offsets']
        self.summaries = json_data.get('summary')
        self.keywords = json_data.get('keywords')
        self.toc = json_data.get('toc')

        if self.add_ner and self.language_ISO:
            cache_key = self._ner_cache_key(self.language_ISO)
            cached_model = self.ner_model_cache.get(cache_key)
            if cached_model is not None:
                self.file_ner_models[file] = cached_model

        return True

    def _export_current_file(self, file: Path):
        """
        Export outputs for the currently loaded file.
        """
        export_target = self.export_format

        if file.suffix.lower() != '.json':
            formats_to_export = (
                [ExportFormats.CSV, ExportFormats.JSON, ExportFormats.HTML]
                if export_target == ExportFormats.ALL
                else [export_target, ExportFormats.JSON]
            )
        else:
            formats_to_export = (
                [ExportFormats.CSV, ExportFormats.HTML]
                if export_target == ExportFormats.ALL
                else [export_target]
            )

        try:
            for export_format in formats_to_export:
                self.export_format = export_format
                writer = output_utils.get_writer(self)
                writer.write()

            print('[blue][bold]... DONE')

        except ValueError as err:
            print(f'... {err}')
        except Exception as err:
            print(f'... An unexpected error occurred: {err}')
        finally:
            self.export_format = self._base_export_format

    async def process_files(
        self,
        ner_model_cache: dict[str, object] | None = None
    ):
        """
        Process every file assigned to the processor.
        """
        if ner_model_cache is not None:
            self.ner_model_cache = ner_model_cache

        if not self.files_to_process:
            return

        total_files = len(self.files_to_process)

        for idx, file in enumerate(self.files_to_process, start=1):
            self.current_input_file = file
            self._reset_base_params()

            if file.suffix.lower() == '.json':
                if not self._prepare_from_json(file):
                    continue
            else:
                msg = (
                    "[bold][orange]... "
                    f"[{idx}/{total_files}] Dygesting {file.name}"
                )
                print(msg)
                await self.process_file(file)

            self._export_current_file(file)

        self.current_input_file = None

    async def process_file(self, file: Path):
        """
        Async version of process_file.
        Main function for processing files and creating TOCs, summaries,
        keywords as well as running NER.
        """
        # Reset processing values
        self._reset_processing_vals()

        # Get filename and output filepath
        self.filename = file.stem
        self.output_filepath = self.output_dir.joinpath(self.filename)

        # Load file
        self.text = self.run_with_error_handling(
            utils.load_file,
            file,
            self.verbose,
            error_message="Error during file loading"
        )

        # Chunk file
        self.chunks, self.token_count, self.sentence_offsets = (
            self.run_with_error_handling(
                utils.chunk_text,
                text=self.text,
                chunk_size=self.chunk_size,
                error_message="Error during text chunking"
                )
            )

        if self.verbose:
            print(f"... Total tokens in file: {self.token_count}")
            print(f"... Number of chunks: {len(self.chunks)}")

        # Run language detection
        if not self.language_ISO:
            self.language_ISO = self.run_with_error_handling(
                self.run_language_detection,
                error_message="Error during language detection"
            )

            # Transform ISO code to string ('en' → 'English')
            self.language_string = LANGUAGES.get(self.language_ISO).title()

        # Run Named Entity Recognition (NER)
        if self.add_ner:
            self.entities = self.run_with_error_handling(
                self.run_ner,
                error_message="Error during NER task"
            )

        # Create TOC (Table of Contents)
        if self.add_toc:
            self.toc = await self.create_toc_async()

        # Create summary and keywords in one go
        if self.add_summaries and self.add_keywords:
            self.summaries, self.keywords = (
                await self.create_summaries_and_keywords_async()
            )

        # Create only summary
        elif self.add_summaries:
            self.summaries = await self.create_summaries_async()

        # Create only keywords
        elif self.add_keywords:
            self.keywords = await self.generate_keywords_async()

    def run_with_error_handling(
        self,
        func,
        *args,
        error_message="",
        **kwargs
    ):
        """
        Helper function to handle exceptions uniformly.
        """
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[purple]... {error_message}: {e}")
            print(f"[purple]{traceback.format_exc()}")
            raise typer.Exit(code=1)


class SummaryProcessor:
    def __init__(
            self,
            summaries: Optional[dict[str]] = None,
            keywords: Optional[set[str]] = None,
            embedding_model: str = None,
            key: str = 'topic',
            threshold: float = 0.8,
            verbose: bool = False
    ):
        """
        Initialize the SummaryProcessor and process the summaries.

        Args:
            summaries (list[dict]): List of summary dictionaries.
            embedding_model (str): The name of the embedding model to use.
            key (str): The key in the dictionary to embed (e.g., 'topic').
            threshold (float): Cosine similarity threshold to consider
            topics as similar.
        """
        self.embedding_model = embedding_model
        self.key = key
        self.threshold = threshold
        self.summaries = summaries
        self.keywords = keywords
        self.verbose = verbose

        self.embedded_summaries = {}
        self.filtered_summaries = []
        self.embedded_keywords = {}
        self.filtered_keywords = []

    async def embed_summaries(self):
        """
        Embed summaries.
        """
        for summary in self.summaries:
            text = summary[self.key]
            response = await llms.get_aembeddings(
                text,
                model=self.embedding_model
            )
            self.embedded_summaries[text] = np.array(response)

    async def embed_keywords(self):
        """
        Embed strings (like keywords).
        """
        for keyword in self.keywords:
            response = await llms.get_aembeddings(
                keyword,
                model=self.embedding_model
            )
            self.embedded_keywords[keyword] = np.array(response)

    async def batch_embed_summaries(self, batch_size: int = 10):
        """
        Embed summaries in batches for better performance.

        Args:
            batch_size (int): Number of summaries to process in parallel.
            Default is 10.
        """
        if not self.summaries:
            return

        # Create batches of summaries
        batches = []
        for i in range(0, len(self.summaries), batch_size):
            batches.append(self.summaries[i:i + batch_size])

        for batch in batches:
            # Create tasks for each summary in the batch
            tasks = []
            for summary in batch:
                text = summary[self.key]
                tasks.append(llms.get_aembeddings(
                    text,
                    model=self.embedding_model)
                )

            # Process all tasks in parallel
            responses = await asyncio.gather(*tasks)

            # Store results
            for summary, response in zip(batch, responses):
                text = summary[self.key]
                self.embedded_summaries[text] = np.array(response)

    async def batch_embed_keywords(self, batch_size: int = 10):
        """
        Embed keywords in batches for better performance.

        Args:
            batch_size (int): Number of keywords to process in parallel.
            Default is 10.
        """
        if not self.keywords:
            return

        # Create batches of keywords
        batches = []
        for i in range(0, len(self.keywords), batch_size):
            batches.append(list(self.keywords[i:i + batch_size]))

        for batch in batches:
            # Create tasks for each keyword in the batch
            tasks = []
            for keyword in batch:
                tasks.append(llms.get_aembeddings(
                    keyword,
                    model=self.embedding_model)
                )

            # Process all tasks in parallel
            responses = await asyncio.gather(*tasks)

            # Store results
            for keyword, response in zip(batch, responses):
                self.embedded_keywords[keyword] = np.array(response)

    @staticmethod
    def cosine_similarity(vec1, vec2):
        """
        Calculate the cosine similarity between two vectors.

        Args:
            vec1 (np.array): First embedding vector.
            vec2 (np.array): Second embedding vector.

        Returns:
            float: Cosine similarity score.
        """
        dot_product = np.dot(vec1, vec2)
        norm_vec1 = np.linalg.norm(vec1)
        norm_vec2 = np.linalg.norm(vec2)
        if norm_vec1 == 0 or norm_vec2 == 0:
            return 0.0
        return dot_product / (norm_vec1 * norm_vec2)

    def remove_similar_summaries(self):
        """
        Remove similar summaries based on cosine similarity of their topics.

        Returns:
            list[dict]: Filtered list of summaries with similar topics removed.
        """
        similar_topics = []

        # Generate all unique pairs of topics
        for (topic1, emb1), (topic2, emb2) in combinations(
            self.embedded_summaries.items(),
            2
        ):
            similarity = self.cosine_similarity(emb1, emb2)
            if similarity >= self.threshold:
                similar_topics.append({
                    'topic_1': topic1,
                    'topic_2': topic2,
                    'similarity_score': similarity
                })

        # Identify Topics to Remove (topic_2 in each similar pair)
        topics_to_remove = set(pair['topic_2'] for pair in similar_topics)

        # Filter out summaries with topics to remove
        filtered_summaries = []
        for summary in self.summaries:
            if summary[self.key] not in topics_to_remove:
                filtered_summaries.append(summary)

        # Display Similar Topics Identified
        if self.verbose:
            if similar_topics:
                print("... Similar Topics Identified:")
                for pair in similar_topics:
                    msg = (
                        f"... '{pair['topic_1']}' <--> '{pair['topic_2']}' "
                        f"with score {pair['similarity_score']:.4f}"
                    )
                    print(msg)
            else:
                print("... No similar topics found above the threshold.")

        return filtered_summaries

    def remove_similar_keywords(self):
        """
        Remove similar keywords based on cosine similarity of their embeddings.

        Returns:
            list[str]: A filtered list of keywords with similar ones removed.
        """
        similar_pairs = []

        # Generate all unique pairs of keywords and check their similarity
        for (kw1, emb1), (kw2, emb2) in combinations(
            self.embedded_keywords.items(),
            2
        ):
            similarity = self.cosine_similarity(emb1, emb2)
            if similarity >= self.threshold:
                similar_pairs.append({
                    'keyword_1': kw1,
                    'keyword_2': kw2,
                    'similarity_score': similarity
                })

        # Identify keywords to remove.
        keywords_to_remove = set(pair['keyword_2'] for pair in similar_pairs)

        # Filter out the similar keywords
        filtered_keywords = (
            [k for k in self.keywords if k not in keywords_to_remove]
        )

        # Display similar keywords if verbose is enabled
        if self.verbose:
            if similar_pairs:
                print("... Similar Keywords Identified:")
                for pair in similar_pairs:
                    msg = (
                        f"... '{pair['keyword_1']}' <--> '{pair['keyword_2']}'"
                        f" with score {pair['similarity_score']:.4f}"
                    )
                    print(msg)
            else:
                print("... No similar keywords found above the threshold.")

        return filtered_keywords

    async def get_filtered_summaries(self):
        """
        Get the filtered summaries.

        Returns:
            list[dict]: Filtered summaries.
        """
        # await self.embed_summaries()
        await self.batch_embed_summaries()
        self.filtered_summaries = self.remove_similar_summaries()
        return self.filtered_summaries

    async def get_filtered_keywords(self):
        """
        Get the filtered keywords.

        Returns:
            list[str]: Filtered keywords.
        """
        # await self.embed_keywords()
        await self.batch_embed_summaries()
        self.filtered_keywords = self.remove_similar_keywords()
        return self.filtered_keywords
