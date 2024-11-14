import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
        filters,
        ApplicationBuilder,
        ContextTypes,
        CommandHandler,
        MessageHandler
        )

from saverbot.parser import parser
from saverbot.scripts.dowload import download


logging.basicConfig(
        level=logging.INFO,
        filemode=f'{__name__}.log',
        format='%(asctime)s %(levelname)s %(message)s',
        )

load_dotenv()
token = os.getenv('BOT_TOKEN')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """Hi! I can dowload any media from Instagram,
Tiktok and Pintrest by link.
Available actions:
/start - itroduction
/info - instruction"""
    await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text
            )


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """Give bot full url of any tiktok/instagram/pintrest media
and it will download and send it to you as message.
1. Url must start with https://
2. Bot is working in test mode"""
    await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text
            )


async def send_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = parser.parse_url(update.message.text)
    if text:
        filename = await download(text)
        await context.bot.send_document(
                chat_id=update.effective_chat.id,
                document=open(filename, 'rb')
                )
    else:
        await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='I require correct URL'
                )


def main():
    application = ApplicationBuilder().token(token).build()
    start_handler = CommandHandler(
            'start',
            start
            )
    url_handler = MessageHandler(
            filters.TEXT & (~filters.COMMAND),
            send_media
            )

    application.add_handler(start_handler)
    application.add_handler(url_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
