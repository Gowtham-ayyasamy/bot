from telegram.ext import Updater, MessageHandler, Filters
import os

TOKEN = os.environ['7542836224:AAFa68zmbXLnfDaTKdJ8DoiFZbO1-jWEvmk']
GROUP_A_ID = int(os.environ['-4621356734'])
GROUP_B_ID = int(os.environ['-4957496536'])

def forward_message(update, context):
    from_chat_id = update.effective_chat.id
    message = update.effective_message

    if from_chat_id == GROUP_A_ID:
        context.bot.send_message(chat_id=GROUP_B_ID, text=message.text)
    elif from_chat_id == GROUP_B_ID:
        context.bot.send_message(chat_id=GROUP_A_ID, text=message.text)

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message))
updater.start_polling()
updater.idle()
