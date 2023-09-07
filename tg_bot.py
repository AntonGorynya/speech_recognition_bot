import logging
import telegram

from environs import Env
from telegram.ext import Updater, ConversationHandler, CommandHandler, MessageHandler, Filters
from dialog_flow_common import detect_intent_text
from log_handler import TelegramLogsHandler


logger = logging.getLogger('telegram_logger')


def start(update, _):
    username = update.message.chat['username']
    update.message.reply_text(f'Привет {username}!')
    echo(update, _)


def cancel(update, _):
    update.message.reply_text(
        'До новых встреч!',
    )
    return ConversationHandler.END


def echo(update, context):
    chat_id = update['message']['chat']['id']
    text = update['message']['text']
    response = detect_intent_text(project_id, chat_id, text)
    if not response.query_result.intent.is_fallback:
        update.message.reply_text(response.query_result.fulfillment_text)


if __name__ == '__main__':
    env = Env()
    env.read_env()
    bot_token = env('TG_TOKEN')
    google_key = env('GOOGLE_KEY')
    project_id = env('PROJECT_ID')
    log_bot_token = env('TELEGRAM_LOG_BOT_TOKEN')
    chat_id = env('LOG_CHAT_ID')

    logging.basicConfig(level=logging.DEBUG)
    log_bot = telegram.Bot(token=log_bot_token)
    logger.addHandler(TelegramLogsHandler(log_bot, chat_id))

    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('cancel', cancel))
    dispatcher.add_handler(CommandHandler('start', start, run_async=True))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()
