from yt_dlp import YoutubeDL
import instaloader


OPTS = {
        'allow_unplayable_formats': False,
        'restrictfilenames': True,
        'windowsfilenames': True,
        'verbose': True,
        }


async def tt_download(url: str, **kwargs) -> str:
    opts = OPTS.copy()
    opts.update(kwargs)
    with YoutubeDL(opts) as loader:
        info_dict = loader.extract_info(url, download=True)
        file_name = loader.prepare_filename(info_dict)
        return file_name


async def inst_loader(url: str, **kwargs) -> str:
       pass 
