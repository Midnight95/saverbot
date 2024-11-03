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

from parser import parser


logging.basicConfig(
        level=logging.INFO,
        filemode=f'{__name__}.log',
        format='%(asctime)s %(levelname)s %(message)s',
        )

load_dotenv()
token = os.getenv('BOT_TOKEN')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = '''
    Hi! I can dowload any media from Instagram, Tiktok and Pintrest by link.
    I also can download whole profiles but require $$motivation$$
    '''
    await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text
            )


async def process_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = parser.parse_url(update.message.text)
    await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text if text else update.message.text
            )


if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler(
            'start',
            start
            )
    echo_handler = MessageHandler(
            filters.TEXT & (~filters.COMMAND),
            process_text
            )

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.run_polling()
