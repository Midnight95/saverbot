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


async def process_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = parser.parse_url(update.message.text)
    if text:
        await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=text
                )
    else:
        await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='I require URL'
                )


def main():
    application = ApplicationBuilder().token(token).build()
    start_handler = CommandHandler(
            'start',
            start
            )
    url_handler = MessageHandler(
            filters.TEXT & (~filters.COMMAND),
            process_text
            )

    application.add_handler(start_handler)
    application.add_handler(url_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
