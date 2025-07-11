import telebot
# from bs4 import BeautifulSoup

bot = telebot.TeleBot('8076010446:AAG-SVl8iqKDoRxmUcAq6EkOfiWQID1mzf4')

@bot.message_handler(commands=['startproject'])
def send_welcome(message):
	bot.reply_to(message, "Write a project name")
	bot.register_next_step_handler(message, projectfunction);
def projectfunction(message):
	global projectname
	projectname = message.text
	bot.infinity_polling()
	with open('template.html') as old, open(projectname + '.html', 'w') as new:
		lines = old.readlines()
		for i in range(len(lines)):
			print(lines[i], file=new)
	bot.send_message(message.from_user.id, 'Project successfully created')
bot.infinity_polling()