from yt_dlp import YoutubeDL
import instaloader
import os


OPTS = {
        'allow_unplayable_formats': False,
        'restrictfilenames': True,
        'windowsfilenames': True,
        'verbose': True,
        }

INSTAGRAM_SESSION = [i for i in os.listdir() if i.startswith('session')][0]


async def tt_download(url: str, **kwargs) -> str:
    opts = OPTS.copy()
    opts.update(kwargs)
    with YoutubeDL(opts) as loader:
        info_dict = loader.extract_info(url, download=True)
        file_name = loader.prepare_filename(info_dict)
        return file_name


async def inst_loader(url: str, **kwargs) -> str:
    loader = instaloader.Instaloader()
    loader.load_session_from_file(
            username=INSTAGRAM_SESSION[INSTAGRAM_SESSION.find('-')+1:],
            filename=INSTAGRAM_SESSION
            )

    shorcode = url[url.rfind('p/')+2:]
    post = instaloader.Post.from_shortcode(loader.context, shorcode)
    loader.download_post(post, shorcode)
    return shorcode
