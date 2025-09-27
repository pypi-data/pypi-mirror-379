import typer
import asyncio
from typing import Optional
from pathlib import Path
from rich import print
from dygest import utils
from dygest.output_utils import ExportFormats


app = typer.Typer(
    no_args_is_help=True,
    help='DYGEST: Document Insights Generator 🌞',
    add_completion=False
)


@app.command("config", no_args_is_help=True)
def configure(
    add_custom: Optional[str] = typer.Option(
        None,
        "--add_custom",
        "-add",
        help="Add a custom key-value pair to the .env (format: KEY=VALUE).",
    ),
    light_model: str = typer.Option(
        None,
        "--light_model",
        "-l",
        help="LLM model name for lighter tasks (summarization, keywords)",
    ),
    expert_model: str = typer.Option(
        None,
        "--expert_model",
        "-x",
        help="LLM model name for heavier tasks (TOCs).",
    ),
    embedding_model: str = typer.Option(
        None,
        "--embedding_model",
        "-e",
        help="Embedding model name.",
    ),
    temperature: float = typer.Option(
        None,
        "--temperature",
        "-t",
        help='Temperature of LLM.',
    ),
    sleep: float = typer.Option(
        None,
        "--sleep",
        "-s",
        help='Pause LLM requests to prevent rate limit errors (in seconds).',
    ),
    chunk_size: int = typer.Option(
        None,
        "--chunk_size",
        "-c",
        help="Maximum number of tokens per chunk."
    ),
    ner: Optional[bool] = typer.Option(
        None,
        "--ner/--no-ner",
        help="Enable Named Entity Recognition (NER). Defaults to False.",
    ),
    precise: Optional[bool] = typer.Option(
        None,
        "--precise/--fast",
        help="Enable precise mode for NER. Defaults to fast mode.",
    ),
    language: str = typer.Option(
        None,
        "--lang",
        "-lang",
        help='Language of file(s) for NER. Defaults to auto-detection.',
    ),
    view_config: bool = typer.Option(
        False,
        "--view_config",
        "-v",
        help="View loaded config parameters.",
    )
):
    """
    Configure LLMs, Embeddings and Named Entity Recognition.
    (Config file: .env)
    """
    from dygest.ner_utils import NERlanguages
    from dygest.config import (
        print_config,
        ENV_FILE,
        set_key,
        validate_model_name
    )

    if view_config:
        print_config()
        return

    if light_model is not None:
        if not validate_model_name(light_model):
            typer.secho(
                f"Invalid light model name format: '{light_model}'\n"
                "Model name must be in one of these formats:\n"
                "- 'provider/model' (e.g. 'ollama/qwen2.5:latest')\n"
                "- 'openai/provider/model' (e.g. 'openai/providerX/qwen2.5')",
                fg=typer.colors.RED
            )
            raise typer.Exit(code=1)
        set_key(ENV_FILE, 'LIGHT_MODEL', light_model)

    if expert_model is not None:
        if not validate_model_name(expert_model):
            typer.secho(
                f"Invalid expert model name format: '{expert_model}'\n"
                "Model name must be in one of these formats:\n"
                "- 'provider/model' (e.g. 'ollama/qwen2.5:latest')\n"
                "- 'openai/provider/model' (e.g. 'openai/providerX/qwen2.5')",
                fg=typer.colors.RED
            )
            raise typer.Exit(code=1)
        set_key(ENV_FILE, 'EXPERT_MODEL', expert_model)

    if embedding_model is not None:
        if not validate_model_name(embedding_model):
            typer.secho(
                f"Invalid embedding model name format: '{embedding_model}'\n"
                "Model name must be in one of these formats:\n"
                "- 'provider/model' (e.g. 'ollama/qwen2.5:latest')\n"
                "- 'openai/provider/model' (e.g. 'openai/providerX/qwen2.5')",
                fg=typer.colors.RED
            )
            raise typer.Exit(code=1)
        set_key(ENV_FILE, 'EMBEDDING_MODEL', embedding_model)

    if temperature is not None:
        set_key(ENV_FILE, 'TEMPERATURE', str(temperature))

    if sleep is not None:
        set_key(ENV_FILE, 'SLEEP', str(sleep))

    if chunk_size is not None:
        set_key(ENV_FILE, 'CHUNK_SIZE', str(chunk_size))

    if ner is not None:
        set_key(ENV_FILE, 'NER', str(ner).lower())

    if precise is not None:
        set_key(ENV_FILE, 'NER_PRECISE', str(precise).lower())

    # Add language to NER CONFIG if provided
    if language is not None:
        try:
            lang_value = NERlanguages(language).value
            set_key(ENV_FILE, 'NER_LANGUAGE', lang_value)
        except ValueError:
            typer.secho(
                f"... '{language}' is not a valid NER language. Using 'auto'.",
                fg=typer.colors.MAGENTA
            )
            set_key(ENV_FILE, 'NER_LANGUAGE', NERlanguages.AUTO.value)

    # Handle custom key-value pair if provided
    if add_custom is not None:
        if '=' not in add_custom:
            typer.secho(
                "... Error: Custom key-value pair must be in format KEY=VALUE",
                fg=typer.colors.RED
            )
            raise typer.Exit(code=1)

        key, value = add_custom.split('=', 1)
        key = key.strip()
        value = value.strip()

        if not key:
            typer.secho(
                "... Error: Key cannot be empty",
                fg=typer.colors.RED
            )
            raise typer.Exit(code=1)

        # Add custom key-value pair
        set_key(ENV_FILE, key, value)

    # Print updated config
    print_config()


@app.command("run", no_args_is_help=True)
def main(
    filepath: str = typer.Option(
        None,
        "--files",
        "-f",
        help="Path to the input folder or file."
    ),
    output_dir: Optional[str] = typer.Option(
        None,
        "--output_dir",
        "-o",
        help="If not provided, outputs will be saved in the input folder.",
    ),
    export_format: Optional[ExportFormats] = typer.Option(
        ExportFormats.HTML,
        "--export_format",
        "-ex",
        help="Set the data format for exporting.",
    ),
    toc: bool = typer.Option(
        False,
        "--toc",
        "-t",
        help="Create a Table of Contents for the text. Defaults to False.",
    ),
    summarize: bool = typer.Option(
        False,
        "--summarize",
        "-s",
        help="Include a short summary for the text. Defaults to False.",
    ),
    keywords: bool = typer.Option(
        False,
        "--keywords",
        "-k",
        help="Create descriptive keywords for the text. Defaults to False.",
    ),
    sim_threshold: float = typer.Option(
        0.85,
        "--sim_threshold",
        "-sim",
        help="Similarity threshold for removing duplicate topics."
    ),
    html_template_default: utils.DefaultTemplates = typer.Option(
        utils.DefaultTemplates.tabs,
        "--default_template",
        "-dt",
        help="Choose a built-in HTML template ('tabs' or 'plain')."
    ),
    html_template_user: Optional[Path] = typer.Option(
        None,
        "--user_template",
        "-ut",
        help="Provide a custom folder path for an HTML template.",
        file_okay=False,
        dir_okay=True,
        resolve_path=True
    ),
    skip_html: bool = typer.Option(
        False,
        "--skip_html",
        "-skip",
        help="Skip file(s) if an HTML already exists in same folder. \
Defaults to False.",
    ),
    export_metadata: bool = typer.Option(
        False,
        "--export_metadata",
        "-meta",
        help="Enable exporting metadata to output file(s). Defaults to False.",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Enable verbose output. Defaults to False.",
    )
):
    """
    Create insights for your documents (summaries, keywords, TOCs).
    """
    from dygest import core, utils
    from dygest.ner_utils import NERlanguages
    from dygest.config import missing_config_requirements, get_config_value

    # Check if required configuration is set
    if missing_config_requirements():
        msg = (
            "[purple]... Please configure dygest first by running"
            "*dygest config* and set your LLMs."
        )
        typer.secho(msg, fg=typer.colors.RED)
        raise typer.Exit(code=1)

    # Determine which HTML template folder to use
    if html_template_user is not None:
        chosen_template = html_template_user
    else:
        # Use built-in template based on the name
        try:
            chosen_template = utils.default_html_template(
                html_template_default.value
            )
        except ValueError as e:
            typer.secho(f"... Error: {e}", fg=typer.colors.RED)
            raise typer.Exit(code=1)

    # Validate HTML template path
    if export_format in [ExportFormats.HTML, ExportFormats.ALL]:
        if not chosen_template.exists():
            error_msg = (
                "... Error: HTML template folder does not exist: "
                f"{chosen_template}"
            )
            typer.secho(
                error_msg,
                fg=typer.colors.RED
            )
            raise typer.Exit(code=1)
        html_file = next(chosen_template.glob('*.html'), None)
        if not html_file:
            error_msg = (
                "... Error: No HTML file found in template path: "
                f"{chosen_template}"
            )
            typer.secho(
                error_msg,
                fg=typer.colors.RED
            )
            raise typer.Exit(code=1)

    # Create a list of all files to process
    files_to_process = utils.load_filepath(filepath, skip_html=skip_html)

    if not files_to_process:
        raise typer.Exit(code=1)

    processor = core.DygestProcessor(
        filepath=filepath,
        output_dir=utils.resolve_input_dir(Path(filepath), output_dir),
        light_model=get_config_value('LIGHT_MODEL'),
        expert_model=get_config_value('EXPERT_MODEL'),
        embedding_model=get_config_value('EMBEDDING_MODEL'),
        temperature=get_config_value('TEMPERATURE', 0.0, float),
        sleep=get_config_value('SLEEP', 0.0, float),
        chunk_size=get_config_value('CHUNK_SIZE', 0, int),
        add_toc=toc,
        add_summaries=summarize,
        add_keywords=keywords,
        add_ner=get_config_value('NER', False, bool),
        sim_threshold=sim_threshold,
        provided_language=get_config_value('NER_LANGUAGE', NERlanguages.AUTO),
        precise=get_config_value('NER_PRECISE', False, bool),
        verbose=verbose,
        export_metadata=export_metadata,
        export_format=export_format,
        html_template_path=chosen_template,
        files_to_process=files_to_process
    )

    # Run async processing
    asyncio.run(processor.process_files())


if __name__ == '__main__':
    try:
        app()
    except KeyboardInterrupt:
        print("\n... Operation cancelled by user")
    except Exception as e:
        print(f"\n... An error occurred: {e}")
