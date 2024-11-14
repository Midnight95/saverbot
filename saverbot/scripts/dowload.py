from yt_dlp import YoutubeDL
import dotenv
import os

dotenv.load_dotenv()


OPTS = {
        'allow_unplayable_formats': False,
        'restrictfilenames': True,
        'windowsfilenames': True,
        'verbose': True,
        }

INSTAGRAM_CREDENTIALS = {
        'username': os.getenv('INSTAGRAM_USERNAME'),
        'password': os.getenv('INSTAGRAM_PASSWORD')
        }


async def download(url: str) -> str:
    with YoutubeDL(OPTS) as loader:
        info_dict = loader.extract_info(url, download=True)
        file_name = loader.prepare_filename(info_dict)
        return file_name


def instagram_auth(username, password):
    pass
