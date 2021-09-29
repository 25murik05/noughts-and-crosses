import telebot
from config import value, TOKEN
from clases import CryptoConverter, ConvertionExeption


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \
    <в какую валюту перевести> \
    <количество переводимой валюты> \n Увидить список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands='values')
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for v in value.keys():
        text = '\n'.join((text, v, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types='text', )
def convert(message: telebot.types.Message):
    try:
        val = message.text.split(' ')
        if len(val) != 3:
            raise ConvertionExeption('Параметров не нужное колличество!!')

        quote, base, amount = val  ## Выводим валюту, валюту которую перевести, и сколько валюты
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionExeption as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} равна: {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
