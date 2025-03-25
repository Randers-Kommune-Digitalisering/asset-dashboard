import os
from dotenv import load_dotenv


# loads .env file, will not overide already set enviroment variables (will do nothing when testing, building and deploying)
load_dotenv()


DEBUG = os.getenv('DEBUG', 'False') in ['True', 'true']
PORT = os.getenv('PORT', '8080')
POD_NAME = os.getenv('POD_NAME', 'pod_name_not_set')

# Keycloack Auth
# KEYCLOAK_URL = os.environ["KEYCLOAK_URL"].strip()
# KEYCLOAK_REALM = os.environ["KEYCLOAK_REALM"].strip()
# KEYCLOAK_CLIENT_ID = os.environ["KEYCLOAK_CLIENT_ID"].strip()

# Database
ASSET_DB_HOST = os.getenv("ASSET_DB_HOST")
ASSET_DB_USER = os.getenv("ASSET_DB_USER")
ASSET_DB_PASS = os.getenv("ASSET_DB_PASS")
ASSET_DB_DATABASE = os.getenv("ASSET_DB_DATABASE")
ASSET_DB_PORT = os.getenv("ASSET_DB_PORT")
