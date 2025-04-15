# Set your Google Cloud Project ID
export GOOGLE_CLOUD_PROJECT="REPLACE-WITH-YOUR-PROJECT-ID"

# Set your desired Google Cloud Location
export GOOGLE_CLOUD_LOCATION="REPLACE-WITH-YOUR-REGION"

# Set the name for your Cloud Run service
export SERVICE_NAME="auto-insurance-agent-service"

# Set the agent name
export APP_NAME="auto_insurance_agent"

# Set the path to your agent code directory
export AGENT_PATH="./auto_insurance_agent"

adk deploy cloud_run \
--project=$GOOGLE_CLOUD_PROJECT \
--region=$GOOGLE_CLOUD_LOCATION \
--service_name=$SERVICE_NAME \
--app_name=$APP_NAME \
--with_ui \
$AGENT_PATH