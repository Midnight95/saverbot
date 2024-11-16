from yt_dlp import YoutubeDL


OPTS = {
        'allow_unplayable_formats': False,
        'restrictfilenames': True,
        'windowsfilenames': True,
        'verbose': True,
        }


async def download(url: str, **kwargs) -> str:
    opts = OPTS.copy()
    opts.update(kwargs)
    print('THIS IS OPTS', opts, '\n\n\n\n\n\n\n\n\n')
    with YoutubeDL(opts) as loader:
        info_dict = loader.extract_info(url, download=True)
        file_name = loader.prepare_filename(info_dict)
        return file_name
