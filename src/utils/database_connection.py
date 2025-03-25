from utils.database import DatabaseClient
from utils.config import ASSET_DB_DATABASE, ASSET_DB_USER, ASSET_DB_PASS, ASSET_DB_HOST, ASSET_DB_PORT


def get_asset_db():
    return DatabaseClient(
        db_type='postgresql',
        database=ASSET_DB_DATABASE,
        username=ASSET_DB_USER,
        password=ASSET_DB_PASS,
        host=ASSET_DB_HOST,
        port=ASSET_DB_PORT
    )
