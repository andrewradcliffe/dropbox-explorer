from dotenv import load_dotenv
import os

DROPBOX_TOKEN = ""
DROPBOX_APP_KEY = ""
DROPBOX_APP_SECRET = ""
DROPBOX_TEAM_MEMBER_ID = ""
DOWNLOAD_PATH = ""

def get_variables():
    load_dotenv()
    global DROPBOX_TOKEN, DROPBOX_APP_KEY, DROPBOX_APP_SECRET, DROPBOX_TEAM_MEMBER_ID, DOWNLOAD_PATH
    DROPBOX_TOKEN = os.getenv('DROPBOX_TOKEN')
    DROPBOX_APP_KEY = os.getenv('DROPBOX_APP_KEY')
    DROPBOX_APP_SECRET = os.getenv('DROPBOX_APP_SECRET')
    DROPBOX_TEAM_MEMBER_ID = os.getenv('DROPBOX_TEAM_MEMBER_ID')
    DOWNLOAD_PATH = os.getenv('DOWNLOAD_PATH')
