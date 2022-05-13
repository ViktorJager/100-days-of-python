import os
from dotenv import load_dotenv

load_dotenv("C:/dev/EnvironmentVariables/.env")  # take environment variables from .env.
api_key = os.getenv("MyAPIKey_MyOtherProject")

print(api_key)
