import dotenv
import os

dotenv.load_dotenv()

SQLITE3_DATABASE_PATH = os.getenv("SQLITE3_DATABASE_PATH")