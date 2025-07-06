# from telegram.ext import Updater, MessageHandler, Filters
# import os



# def forward_message(update, context):
#     from_chat_id = update.effective_chat.id
#     message = update.effective_message

#     if from_chat_id == GROUP_A_ID:
#         context.bot.send_message(chat_id=GROUP_B_ID, text=message.text)
#     elif from_chat_id == GROUP_B_ID:
#         context.bot.send_message(chat_id=GROUP_A_ID, text=message.text)

# updater = Updater(TOKEN, use_context=True)
# dp = updater.dispatcher
# dp.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message))
# updater.start_polling()
# updater.idle()


import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = '7542836224:AAFa68zmbXLnfDaTKdJ8DoiFZbO1-jWEvmk'
GROUP_A_ID = '-4621356734'
GROUP_B_ID = '-4957496536'
async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from_chat_id = update.effective_chat.id
    message = update.effective_message

    if from_chat_id == GROUP_A_ID:
        await context.bot.send_message(chat_id=GROUP_B_ID, text=message.text)
    elif from_chat_id == GROUP_B_ID:
        await context.bot.send_message(chat_id=GROUP_A_ID, text=message.text)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), forward_message))

print("🚀 Bot is running...")
app.run_polling()
