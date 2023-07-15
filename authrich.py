import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import service_account
import vertexai

# Specify the path to the service account key file
key_file = 'apikey.json'

# Load the service account key file
credentials = service_account.Credentials.from_service_account_file(
    key_file,
)

# If the credentials are expired, refresh them
if credentials.expired:
    credentials.refresh(Request())

# Set the credentials for the application
google.auth.default(scopes=['https://www.googleapis.com/auth/cloud-platform'])

def authenticate():
    v_PROJECT_ID="work-mylab-machinelearning"
    v_LOCATION="us-central1"
    v_CREDENTIAL=credentials
    vertexai.init(project=v_PROJECT_ID, location=v_LOCATION, credentials=v_CREDENTIAL)
    #vertexai.init(project=v_PROJECT_ID, location=v_LOCATION)
