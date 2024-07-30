import sqlite3
import config

def get_database_connection():
    connection = sqlite3.connect(config.SQLITE3_DATABASE_PATH)

    return connection