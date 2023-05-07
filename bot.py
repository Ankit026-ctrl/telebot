import os
import logging
from telegram import Message
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = "5836600212:AAEV-zpPsonhsNIJvo0h8wcnY6Nz2sPxWJ0"
WELCOME_MESSAGE = "Welcome to this group, @{}!"

def welcome_handler(update, context):
    new_members = update.message.new_chat_members
    for new_member in new_members:
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=WELCOME_MESSAGE.format(new_member.username))

def error_handler(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome_handler))
    dp.add_error_handler(error_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()