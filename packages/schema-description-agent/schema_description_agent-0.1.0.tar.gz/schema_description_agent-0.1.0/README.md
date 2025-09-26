# Schema Description Agent

The Schema Description Agent is a Python-based tool that automatically generates descriptions for tables and their columns. It analyzes the structure and content of a data file, and then uses a Large Language Model (LLM) to produce accurate and concise documentation.

## Features

- **Statistical Analysis:** Automatically calculates key statistics for each column, such as row count, column count, duplicate rows, missing cells, and more.
- **AI-Powered Descriptions:** Leverages LLMs to generate human-readable descriptions for tables and columns based on the statistical analysis.
- **Configurable:** Easily configure the AI provider, model, and other parameters.
- **Extensible:** Built on a modular framework (`sfn_blueprint`) that allows for easy extension and integration.

## Installation

**Prerequisites**


- [uv](https://docs.astral.sh/uv/getting-started/installation/) – package & environment manager  
  Please refer to the official installation guide for the most up-to-date instructions.  
  For quick setup on macOS/Linux, you can currently use:  
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- [Git](https://git-scm.com/)  

**Steps**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/stepfnAI/schema_description_agent.git
    cd schema_description_agent
    git switch dev
    ```

2.  **Create virtual environment and install dependencies:**
    ```bash
    uv sync --extra dev
    source .venv/bin/activate
    ```

3.  **Clone and install the blueprint dependency:**
    The agent requires the `sfn_blueprint` library. Clone it into a sibling directory.
    ```bash
    cd ../
    git clone https://github.com/stepfnAI/sfn_blueprint.git
    cd sfn_blueprint
    git switch dev
    uv pip install -e .
    ```

4.  **Return to the agent directory:**
    ```bash
    cd ../schema_description_agent
    ```

5.  ** set environment variables:**
    ```bash
    export OPENAI_API_KEY='your_openai_api_key'
    ```

## Testing

To run the tests, use the following command from the root of the `schema_description_agent` directory:

```bash
# Run all tests
pytest tests/ -s

# test agent    
pytest tests/test_agent.py -s

# test agent with sample data
pytest tests/test_agent_with_data.py -s
```

## Usage

Here is a simple example of how to use the agent:

```bash
python examples/basic_usage.py
```


## Configuration

The agent can be configured via the `SchemaDescriptionConfig` class. You can modify the default configuration by passing a `SchemaDescriptionConfig` object to the `SchemaDescriptionAgent` constructor.

**Default Configuration:**

-   `ai_provider`: "openai"
-   `model_name`: "gpt-4o"
-   `temperature`: 0.3
-   `max_tokens`: 4000

**Example of custom configuration:**

```python
from schema_description_agent import SchemaDescriptionAgent, SchemaDescriptionConfig

# Create a custom configuration
config = SchemaDescriptionConfig(
    ai_provider="anthropic",
    model_name="claude-3-opus-20240229",
    temperature=0.5
)

# Create an instance of the agent with the custom configuration
agent = SchemaDescriptionAgent(config=config)
```

