from yt_dlp import YoutubeDL


OPTS = {
        'allow_unplayable_formats': False,
        'restrictfilenames': True,
        'windowsfilenames': True,
        }


def download(url: str):
    with YoutubeDL(OPTS) as loader:
        info = loader.extract_info(url, download=False)
        fn = loader.prepare_filename(info)
        loader.download(url)
        return fn
