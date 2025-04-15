# ADK samples for Apigee & Application Integration

This is a collection of sample AI agents created using Google's [Agent Development Kit](https://google.github.io/adk-docs/) that show how to use ADK's built-in tooling to connect to APIs from [Apigee API hub](https://cloud.google.com/apigee/docs/apihub/what-is-api-hub), or integrations from [Application Integration](https://cloud.google.com/application-integration/docs/overview).

| Agent | Description |
|---|---|
| [auto_insurance_agent](./auto_insurance_agent/agent.py) | A virtual assistant for auto insurance that uses API hub to provide APIs as tools. |

For more information on ADK's API Hub and Application Integration toolsets, see the [documentation](https://google.github.io/adk-docs/tools/google-cloud-tools/).

## Prerequisites

You will need a GCP project with the following services enabled and provisioned:
- Vertex AI
- Apigee API hub

You'll also need to [install](https://cloud.google.com/sdk/docs/install) and [configure](https://cloud.google.com/sdk/docs/authorizing) the Google Cloud SDK, or use [Cloud Shell](https://cloud.google.com/shell/docs).

Your user account will need the [`Vertex AI User`](https://cloud.google.com/vertex-ai/docs/general/access-control#aiplatform.user) and [`Cloud API hub Viewer`](https://cloud.google.com/apigee/docs/apihub/iam-roles#apihub.viewer) roles.

## Instructions

Setup the ADK according to the instructions [here](https://google.github.io/adk-docs/get-started/quickstart/).

Rename the `dotenv-sample` file to `.env` and replace the values in the file with your values. Replace any values in `tools.py` files as needed.

To [run](https://google.github.io/adk-docs/get-started/quickstart/#run-your-agent) the agent you can do one of the following:

1. Run the agent using ADK's built-in web client (open a browser at http://localhost:8000):
```
adk web
```

2. Run the agent from the command line:
```
adk run [agent name]
```

## Deploying to Cloud Run

To deploy the agent to Cloud Run, update the variables in this script and run it:
```
./cloudrun-deploy.sh
```

## Disclaimer

This is not an officially supported Google product.
