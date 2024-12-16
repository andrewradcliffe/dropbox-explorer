from dotenv import load_dotenv
import os

def get_variables():
    load_dotenv()
    return os.getenv('DROPBOX_TOKEN'), os.getenv('DOWNLOAD_PATH')
