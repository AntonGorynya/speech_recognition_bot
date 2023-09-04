from environs import Env
from telegram.ext import Updater, ConversationHandler, CommandHandler, MessageHandler, Filters


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
    print(update)
    update.message.reply_text(update.message.text )



if __name__ == '__main__':
    env = Env()
    env.read_env()
    bot_token = env('TG_TOKEN')

    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('cancel', cancel))
    dispatcher.add_handler(CommandHandler('start', start, run_async=True))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()