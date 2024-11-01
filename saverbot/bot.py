import os
import asyncio
import telegram
from dotenv import load_dotenv


load_dotenv()
bot_token = os.getenv('BOT_TOKEN')
print(bot_token)


async def main():
    bot = telegram.Bot(bot_token)
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())
