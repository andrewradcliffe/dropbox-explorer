from dotenv import load_dotenv
import os

load_dotenv()

DROPBOX_TOKEN = os.getenv("DROPBOX_TOKEN")
DOWNLOAD_PATH = os.getenv("DOWNLOAD_PATH")
