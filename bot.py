from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
BOT_TOKEN = '6820240200:AAGBVWRJJyn82CYv8R6mzJFQtPm8APKCjjU'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your forwarding bot.')

def forward_message(update: Update, context: CallbackContext) -> None:
    # Replace 'TARGET_CHAT_ID' with the actual chat ID where you want to forward messages
    target_chat_id = '4090020882'
    context.bot.forward_message(chat_id=target_chat_id, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

def main() -> None:
    updater = Updater(token=BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.TEXT & ~Filters.COMMAND, forward_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
