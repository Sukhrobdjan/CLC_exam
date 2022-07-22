import requests
from telegram import CallbackQuery, ReplyKeyboardMarkup,InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from bs4 import BeautifulSoup


def start(update:Updater, context:CallbackQuery):
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.username
    context.bot.send_sticker(chat_id=update.message.chat_id, sticker='CAACAgIAAxkBAAEFR8Bi0PGxF1XjkAUGi2QRGE54Am_jbwACMwEAAvcCyA87yuGU7tlOzSkE')
    update.message.reply_text(
        f'Assalomu alaykum, {first_name}\n @{last_name} \n\n 👇👇👇👇👇👇')
    return 1


def info(update:Updater, context:CallbackQuery):
    context.bot.send_message(chat_id = update.message.chat_id, text = '⏳Iltimos biroz kutub turing...')
    context.bot.send_sticker(chat_id=update.message.chat_id, sticker='CAACAgIAAxkBAAEFRP1iz8_1hK5bqKV-O0dlCjyRgkRZ1gACgw8AAuSr-UubVSA1Q28HDykE')
    product = update.message.text.strip()
    URL = f'https://asaxiy.uz/product?key={product}'
    name = requests.get(URL).text
    soup = BeautifulSoup(name, 'lxml')
    library = soup.find_all('div',class_ = 'product__item d-flex flex-column justify-content-between')
    for books in library[:10]:
        
        imge = books.find("div", attrs={"class":"product__item-img"}).find("img")
        img_url = imge['data-src']
        info_books = books.find('h5', class_ = 'product__item__info-title').text.strip()
        price = books.find('span', class_="product__item-price").text.strip()
        context.bot.send_message(chat_id = update.message.chat_id, text = f'Title {info_books} \n{img_url}\n Narxi: {price} \n Narxi: ')

  

  
updater = Updater('2108109066:AAHcl8g2qL5j8ID0MkkCGbc8IRUwfwdX6Ck', use_context=True)
conv_handler = ConversationHandler(
    entry_points = [CommandHandler('start', start)],

    states={
        1: [MessageHandler(Filters.text & (~Filters.command), info),]},
        
        fallbacks=[MessageHandler(Filters.text, start)])


updater.dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()