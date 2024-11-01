from tiktokdl.download_post import get_post
import asyncio


async def download_tt(url: str):
    await get_post(
            url=url,
            download_path='.'
            )


asyncio.run(download_tt('https://www.tiktok.com/@grwm.marta1/video/7404857421178391841?is_from_webapp=1&sender_device=pc'))

