from yt_dlp import YoutubeDL


OPTS = {
        'allow_unplayable_formats': False,
        'restrictfilenames': True,
        'windowsfilenames': True,
        }


def download(url: str):
    with YoutubeDL(OPTS) as loader:
        loader.download(url)
