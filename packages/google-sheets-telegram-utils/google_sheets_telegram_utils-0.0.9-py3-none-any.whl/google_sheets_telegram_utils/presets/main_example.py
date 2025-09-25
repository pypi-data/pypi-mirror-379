import logging
import os
from os.path import join, dirname
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from google_sheets_telegram_utils.utils.connectors.csv_connector import CsvConnector
from google_sheets_telegram_utils.utils.configs.csv_config import CsvConfig
from google_sheets_telegram_utils.utils.factories.handlers_factory import HandlerFactory


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

logger = logging.getLogger(__name__)
dotenv_path = join(dirname(__file__), '../.env')

# Load file from the path.
load_dotenv(dotenv_path)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.message.from_user.first_name}!!')


def main() -> None:
    TOKEN = os.environ.get('TOKEN')
    if not TOKEN:
        raise RuntimeError('Please set TOKEN environment variable')

    connector = CsvConnector(CsvConfig(file='users.csv'))
    register_handler = HandlerFactory.get_register_handler(connector)

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('hello', hello))
    application.add_handler(CommandHandler('register', register_handler))

    application.run_polling()


if __name__ == '__main__':
    main()
