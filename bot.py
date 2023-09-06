import json
from pprint import pprint

from environs import Env
from google.cloud import dialogflow
from google.cloud import api_keys_v2
from google.cloud import language_v1
from google.cloud.api_keys_v2 import Key
from telegram.ext import Updater, ConversationHandler, CommandHandler, MessageHandler, Filters


def detect_intent_text(project_id, session_id, text, language_code='ru-RU'):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    return response


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
    update.message.reply_text(response.query_result.fulfillment_text)



if __name__ == '__main__':
    env = Env()
    env.read_env()
    bot_token = env('TG_TOKEN')
    google_key = env('GOOGLE_KEY')
    project_id = env('PROJECT_ID')


    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('cancel', cancel))
    dispatcher.add_handler(CommandHandler('start', start, run_async=True))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()