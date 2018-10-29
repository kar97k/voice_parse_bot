#import config
#import telebot
import requests
from time import sleep

url = "https://api.telegram.org/bot769918614:AAGJTSc4pHSrAfuzbmKnoNaV2fD8U2OUyx8/"

def get_updates_json(request):
	#params = {'timeout': 10, 'offset': None}
	response = requests.get(request + 'getUpdates')
	return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

chat_id = get_chat_id(last_update(get_updates_json(url)))
send_mess(chat_id, 'Hello from bot')

def main():  
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           send_mess(get_chat_id(last_update(get_updates_json(url))), 'New update')
           update_id += 1
        sleep(60) 

if __name__ == '__main__':  
    main()

'''
bot = telebot.TeleBot(config.token)

@bot.getUpdates(timeout=10)
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
'''