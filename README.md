# Databricks Agent Asset Bundle (DAB)

A comprehensive Databricks Asset Bundle (DAB) that includes both an agent definition/deployment workflow and a chatbot application for interacting with Databricks model serving endpoints.

## Overview

This bundle contains:
1. **Agent Job** - A Databricks job that defines, logs, evaluates, registers, and deploys an MLflow ResponsesAgent with tool-calling capabilities
2. **Chatbot App** - A Dash-based web application providing a user-friendly interface to interact with any Databricks model serving endpoint

## Prerequisites

- Databricks CLI installed (`pip install databricks-cli`)
- Databricks workspace access with Unity Catalog enabled
- Authentication configured (`.databrickscfg` or environment variables)
- Python 3.11+ recommended (Python 3.12+ requires MLflow >= 2.18.0)

## Project Structure

```
.
├── databricks.yml                    # Main bundle configuration
├── resources/
│   └── agent_dab_job.yml            # Job and app definitions
├── notebooks/
│   ├── driver.ipynb                 # Agent definition and deployment workflow
│   ├── agent.py                     # Agent implementation (ResponsesAgent)
│   └── hello_world.ipynb            # Example notebook
└── app/
    ├── app.py                       # Dash application entry point
    ├── app.yaml                     # App deployment configuration
    ├── DatabricksChatbot.py         # Chatbot UI component
    ├── model_serving_utils.py       # Model endpoint query utilities
    └── requirements.txt             # Python dependencies
```

## Setup

1. **Set the Databricks host as an environment variable:**
   ```bash
   export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"
   ```

2. **Authenticate with Databricks:**
   ```bash
   databricks configure --token
   ```

3. **Update configuration files:**
   - In `notebooks/agent.py`: Update `LLM_ENDPOINT_NAME` with your model endpoint
   - In `notebooks/driver.ipynb`: Set the Unity Catalog location (catalog, schema, model_name) for agent registration

## Agent Job

### What It Does

The agent job (`define_deploy_agent_job`) runs the `driver.ipynb` notebook, which:
1. Defines a tool-calling agent using MLflow's `ResponsesAgent`
2. Tests the agent interactively
3. Evaluates the agent using Mosaic AI Agent Evaluation
4. Logs the agent as an MLflow model with proper resource dependencies
5. Registers the agent to Unity Catalog
6. Deploys the agent as a serving endpoint

### Deploy and Run the Job

1. **Validate the bundle:**
   ```bash
   databricks bundle validate
   ```

2. **Deploy the bundle:**
   ```bash
   databricks bundle deploy
   ```

3. **Run the agent job:**
   ```bash
   databricks bundle run define_deploy_agent_job
   ```

### Customizing the Agent

Edit `notebooks/agent.py` to:
- Change the LLM endpoint (`LLM_ENDPOINT_NAME`)
- Modify the system prompt (`SYSTEM_PROMPT`)
- Add or remove tools by updating the `TOOLS` list
- Configure Unity Catalog functions for retrieval or external actions

## Chatbot Application

### What It Does

The Dash-based chatbot application provides:
- Clean, modern UI for chatting with Databricks model serving endpoints
- Free-text input field to specify any model endpoint name
- Support for both foundation models and agent endpoints
- Real-time chat interface with typing indicators
- Message history management with clear functionality

### Local Development

1. **Install dependencies:**
   ```bash
   cd app
   pip install -r requirements.txt
   ```

2. **Run the app locally:**
   ```bash
   python app.py
   ```

3. **Access the app:**
   Open your browser to `http://localhost:8050`

4. **Using the app:**
   - Enter a model endpoint name in the "Model Endpoint Name" field
   - Type your message in the input box
   - Click "Send" or press Enter to chat
   - Click "Clear" to reset the conversation

### Deploy the App

The app is configured for deployment as a Databricks App:

```bash
databricks bundle deploy
```

The app will be deployed according to the configuration in `resources/agent_dab_job.yml` under the `apps` section.

## Model Endpoint Compatibility

The chatbot app works with:
1. **Foundation Models** - Databricks foundation model endpoints (chat task type)
2. **External Models** - External model endpoints with chat completion API
3. **Agent Endpoints** - Deployed agents following the conversational agent schema

See [Databricks documentation](https://docs.databricks.com/machine-learning/model-serving/score-foundation-models.html) for more details.

## Environment Configuration

The bundle uses:
- **Performance-optimized environment** for the agent job
- **Serverless compute** (implied by environment version 4)
- **Workspace authentication** for accessing Unity Catalog and model endpoints

## Troubleshooting

### Python 3.12 Compatibility

If you encounter `AttributeError: module 'pkgutil' has no attribute 'find_loader'`:
- Ensure you're using MLflow >= 2.18.0 (already specified in `requirements.txt`)
- Run `pip install --upgrade mlflow`

### Model Endpoint Errors

If the app fails to connect to a model endpoint:
- Verify the endpoint name is correct
- Ensure the endpoint is deployed and running
- Check that your authentication has access to the endpoint
- Confirm the endpoint supports the chat completion schema

## Resources

- [Databricks Agent Framework Documentation](https://docs.databricks.com/generative-ai/agent-framework/index.html)
- [MLflow ResponsesAgent API](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.pyfunc.html#mlflow.pyfunc.ResponsesAgent)
- [Mosaic AI Agent Evaluation](https://docs.databricks.com/mlflow3/genai/eval-monitor)
- [Databricks Apps Documentation](https://docs.databricks.com/apps/index.html)

