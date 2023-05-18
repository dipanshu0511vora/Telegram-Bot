import telegram.ext

telegramtoken = "5991830387:AAGjMm-B3Um91Ny9719Co4ugFf3hqOHct3s"

updater = telegram.ext.Updater("5991830387:AAGjMm-B3Um91Ny9719Co4ugFf3hqOHct3s", use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Welcome to Telegram Bot")

def help(update, context):
    update.message.reply_text(
        """
        /start -> Welcome to the Channel
        /help -> This particular message 
        /content -> About various songs
        /songs -> bollywood songs
        
        """
    )

def content(update, context):
    update.message.reply_text("we have various playlist of songs")

def Songs(update, context):
    update.message.reply_text("playlist link : https://youtu.be/Ps4aVpIESkc")

dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('song', Songs))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
dispatcher.add_handler(telegram.ext.CommandHandler('content', content))


# updater.start_polling()
updater.start_polling(timeout=60)
updater.idle()
