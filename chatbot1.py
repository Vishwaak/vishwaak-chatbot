from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)
x = os.path.join( '//home', 'xerous' , 'Desktop' , 'chatbot' , 'chatterbot-corpus','chatterbot_corpus' , 'data' , 'english/')
for files in os.listdir (x):
	data = open(x + files , 'r').readlines()
	bot.train(data)
while True:
	msg = raw_input('You : ')
	if msg.strip() != 'bye':
		reply = bot.get_response(msg)
		print 'chatbot :' + reply
		if msg.strip() == 'Bye':
			print('chatbot : bye')
			break
