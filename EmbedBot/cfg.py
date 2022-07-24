import os
from pathlib import Path
from dotenv import load_dotenv


dotenv_path = Path('.env')
if dotenv_path.exists():
    load_dotenv(dotenv_path)

TOKEN = os.environ.get('TOKEN')
PREFIX = os.environ.get('PREFIX')
