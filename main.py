import telebot
import time

TOKEN = '1090606873:AAERQbEAAwhlPf4SqpT4wULrm5T7u5XKmWs'
admin_id = 447360295


def listener(messages):

    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'photo' or m.content_type == 'video'  or m.content_type == 'document':
            tb.send_message(chatid, 'Ваша заявка принята в предложку')
            tb.forward_message(admin_id, chatid, m.message_id)
        elif m.content_type == 'text':
            tb.send_message(chatid,'Отправь мне фото/видео/гифку')


tb = telebot.TeleBot(TOKEN)
tb.set_update_listener(listener)
tb.polling()

tb.polling(none_stop=True)

tb.polling(interval=3)

while True:
    pass
