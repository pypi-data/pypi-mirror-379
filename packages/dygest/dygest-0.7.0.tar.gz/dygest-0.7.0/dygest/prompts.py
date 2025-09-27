# Function for building prompts with kwargs

def build_prompt(template, **kwargs):
    prompt = template
    for key, value in kwargs.items():
        placeholder = '{' + key + '}'
        prompt = prompt.replace(placeholder, value)
    return prompt


# TOC CREATION

GET_TOPICS = """The input text is composed of sentences. The first sentence of this text is globally identified as {first_sentence} and the last sentence as {last_sentence}.

Do not include these sentence numbers in your summary. Instead, reference the location **with the sentence number: "S<number>"**.

Your tasks:
1. Identify the top 2 most important topics discussed in this text.
  - Each topic name should be a concise phrase (no more than 5 words).
  - Focus on main topics and incorporate key named entities (of companies, research departments etc.).
2. For each topic, generate a precise sub-headline (no more than 8 words) with key details.
3. For each topic, identify its primary location within the text. This location **MUST be one of the global sentence identifiers** ranging from {first_sentence} to {last_sentence}. For example, if a topic is most relevant to sentence S48, use "S48" as the location. The format for the location is "S<number>", where <number> is the global sentence number.
4. Return results as JSON **IN {language}**. Do NOT add anything else and use this template without any alterations:
[
  {
    "topic": "Concise Subheading in {language}",
    "summary": "Concise sub-headline in {language}",
    "location": "S<number>"
  },
  ...
]

**Input Text:**
{chunk}"""


CREATE_TOC = """Perform the following tasks on the provided list of summaries and **ALWAYS match their language**:

1. **Create a Table of Contents (TOC):**
   - Group related summaries under concise, relevant headlines.
   - Each headline should encapsulate the theme of its grouped topics.

2. **Maintain Summary Locations:**
   - Do **not** alter the "location" value of any summary.

**Output Requirements:**
- **Format:** JSON
- **Language:** {language}
- **Strictly adhere to the following template and return nothing else:**

[
  {
    "headline": "Headline Name",
    "topics": [
      {
        "summary": "summary",
        "location": "location"
      }
    ]
  },
]

**Input Summaries:**
{toc_parts}"""


# SUMMARY CREATION

CREATE_SUMMARY_AND_KEYWORDS = """Perform the following tasks on the provided text:

1. Generate a summary **IN {language}**:
  - max. 3 sentences with the **most important topics** for the provided text.
2. Incorporate key details in your summary:
  - **Who**: Names of individuals involved.
  - **What**: Description of the events or actions.
  - **When**: Mentioned dates.
  - **Where**: Locations related to the events.
  - **Why**: Purpose or reason behind the events.
3. Generate **2 keywords** that capture the key details of the provided text chunk.
  - ALWAYS limit the number of keywords to **exactly 2** to maintain relevance.
  - Ensure the keywords are **accurate** and **informative**
  - Examples:
      - ["Research Data Management", "KonsortSWD"]
      - ["Wirtschaftsentwicklung", "Humanmedizin"]
      - ["Globalisierung", "Big Data"]
      - ["Medizinische Bildgebung", "HPC Cluster"]

**Output Requirements:**
- **Format:** JSON
- **Language:** {language}
- **Strictly adhere to the following template and return nothing else:**

{
  "summary": "Summary",
  "keywords": ["Keyword 1", "Keyword 2"]
}

**Text Chunk:**
{text_chunk}"""

CREATE_SUMMARY = """Perform the following tasks on the provided text chunk:

1. Generate a **summary of max. 3 sentences** with the **most important topics** for the provided text chunk.
2. Incorporate key details in your summary:
   - **Who**: Names of individuals involved.
   - **What**: Description of the events or actions.
   - **When**: Mentioned dates.
   - **Where**: Locations related to the events.
   - **Why**: Purpose or reason behind the events.
3. Return the results in **{language}**.

**Return ONLY the summary and add nothing else!**

**Text Chunk:**
{text_chunk}"""

COMBINE_SUMMARIES = """Perform the following tasks on the provided list of summaries:

1. Generate a **single summary of maximum 5 sentences** that captures the **most important topics** from all provided summaries.
2. **Remove similar summaries** to ensure the remaining summaries are **unique**.
3. Return the summary in **{language}** as a **plain string**.

Return **ONLY** the single summary.

**Input Summaries:**
{summaries}"""


# KEYWORD CREATION

CREATE_KEYWORDS = """Analyze the following text chunk and generate 2 specific keywords that capture the main topics of the text chunk.

**Requirements:**
1. **Focus key details and main topics** of the text chunk.
2. Ensure keywords are **accurate** and **informative**.
3. Provide keywords **{language}** as the input text.
4. ALWAYS limit the number of keywords to **exactly 2** to maintain relevance.
5. Return the keywords as a list of strings, separated by commas like this:
      - Example 1: ["Research Data Management", "KonsortSWD"]
      - Example 2: ["Wirtschaftsentwicklung", "Humanmedizin"]
      - Example 3: ["Globalisierung", "Big Data"]

Return **ONLY the list of keywords** and **nothing else**.

**Text Chunk:**
{text_chunk}"""
