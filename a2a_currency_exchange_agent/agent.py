import os

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool import MCPToolset, StreamableHTTPConnectionParams
from google.adk.tools.apihub_tool.clients.secret_client import SecretManagerClient

PROJECT_ID=os.getenv("GOOGLE_CLOUD_PROJECT")
APIGEE_HOSTNAME=os.getenv("APIGEE_HOSTNAME")
SECRET=f"projects/{PROJECT_ID}/secrets/exchange-rates-agent-apikey/versions/latest"

secret_manager_client = SecretManagerClient()
apikey_credential_str = secret_manager_client.get_secret(SECRET)

SYSTEM_INSTRUCTION = (
    "You are a specialized assistant for currency conversions. "
    "Your sole purpose is to use the 'get_exchange_rate' tool to answer questions about currency exchange rates. "
    "If the user asks about anything other than currency conversion or exchange rates, "
    "politely state that you cannot help with that topic and can only assist with currency-related queries. "
    "Do not attempt to answer unrelated questions or use tools for other purposes."
)

LITELLM_MODEL = os.getenv('LITELLM_MODEL', 'gemini/gemini-2.5-flash')
root_agent = Agent(
    name='currency_exchange_agent',
    model=LiteLlm(model=LITELLM_MODEL),
    description=('An agent that can help with currency conversions.'),
    instruction=SYSTEM_INSTRUCTION,
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
                url=f"https://{APIGEE_HOSTNAME}/currency-exchange-mcp-proxy",
                headers={"x-api-key": apikey_credential_str}
            )
        )
    ]
)
