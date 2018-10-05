from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)
 
for files in os.listdir ('/home/xerous/Desktop/chatbot\chatterbot-corpus/chatterbot_corpus '):
	data = open('/home/xerous\Desktop/chatbot/chatterbot-corpus/chatterbot_corpus '+ files , 'r').readlines()
	bot.train(data)
while True:
	message = input('You: ')
	if message.strip() != 'bye':
		reply = bot.get_response(message)
		print('chatbot :', reply)
		if message.strip() == 'Bye':
			print('chatbot : bye')
			break
