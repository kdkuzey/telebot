import telebot


Token = "7296389753:AAFYY2bacTWCPNAL07_3trEcIqVQ2lGJ6lE"

bot = telebot.TeleBot(Token)
@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message,'NAMASTE! Welcome to the Chatbot for next step -> /help')

@bot.message_handler(['help'])
def help(message):
    bot.reply_to ( message,  
        """
        /start-> Welcome to the channel
    /help -> This praticular message
    /content -> About to provide various links for Entertainment
    /Online_Games -> In this website you can buy online pc games
    /Offline_Games ->  In this website you can download offline pc games
    /Unloack_games -> In this website you can download offline pc games
    /Movies4K ->  In this website you can download movies and series in 4kSDR
    /Movies ->  In this website you can download Latest Movies
    /Anime -> In this website you can watch anime online
    /Book_pdf -> About to provide various books in PDF formate
    /ReadOnlineComic -> About to provide various comics you can read online
    /OnlineComic -> About to provide various comics you can read online
    /GetComics_MarvelAndDc ->this website you can download comics in pdf formate
    /contact-> contact information
        """)

@bot.message_handler(['content'])
def help(message):
    bot.reply_to ( message,'We have various playlist and download links')


@bot.message_handler(['Online_Games'])
def Online_Games(message):
    bot.reply_to ( message,'Link:- https://store.epicgames.com/en-US/')


@bot.message_handler(['Offline_Games'])
def Offline_Games(message):
    bot.reply_to ( message,'Link:-  https://www.skidrowreloaded.com/')


@bot.message_handler(['Unloack_games'])
def Unloack_games(message):
    bot.reply_to ( message,'Link:- https://steamunlocked.net/')


@bot.message_handler(['Movies4K'])
def Movies4K(message):
    bot.reply_to ( message,'Link:- https://olamovies.baby/')


@bot.message_handler(['Movies'])
def Movies(message):
    bot.reply_to ( message,'Link:- https://katmoviehd.fyi/')


@bot.message_handler(['Anime'])
def Anime(message):
    bot.reply_to ( message,'Link:- https://hianime.to/')


@bot.message_handler(['Book_pdf'])
def Book_pdf(message):
    bot.reply_to ( message,'Link:- https://pdfdrive.com.co/')


@bot.message_handler(['ReadOnlineComic'])
def ReadOnlineComic(message):
    bot.reply_to ( message,'Link:- https://readcomiconline.li/')

@bot.message_handler(['OnlineComic'])
def OnlineComic(message):
    bot.reply_to ( message,'Link:- https://readallcomics.com/')

@bot.message_handler(['GetComics_MarvelAndDc'])
def GetComics_MarvelAndDc(message):
    bot.reply_to ( message,'Link:- https://getcomics.org/')


bot.polling()