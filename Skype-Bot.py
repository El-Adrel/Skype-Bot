#!/usr/bin/env python
import time
import Skype4Py
import random

print "|----------------------------------------------|\n";
print "|        Welcome To Snayer's Skype Bot         |\n";
print "|----------------------------------------------|\n";
def commands(Message, Status):
	if Status == 'SENT' or (Status == 'RECEIVED'): 
		
		if Message.Body == "!ping":
			cmd_ping(Message)
		
		elif Message.Body == "!addpeng":
			cmd_addpeng(Message)
		
		elif Message.Body == "!celebrate":
			cmd_celebrate(Message)
		
		elif Message.Body == "!hammertime":
			cmd_hammertime(Message)
		
		elif Message.Body == "!credit":
			cmd_credit(Message)
		
		elif Message.Body == "!help":
			cmd_help(Message)
		
		elif Message.Body == "!spam":
			cmd_spam(Message)
		
		elif Message.Body == "!introduce":
			cmd_intro(Message)
		
		elif Message.Body == '!dice':
			cmd_dice(Message)
		
		elif Message.Body == '!goodjob':
			cmd_goodjob(Message)
			
		elif Message.Body == '!die':
			cmd_die(Message)
		
		elif Message.Body == "!party":
			cmd_party(Message)
	
		else:
			pass
	
	else:
		pass

def cmd_ping(Message):
	Message.Chat.SendMessage('Robot: Yes, I\'m still alive. :)')
	print "Ping Command Received \n"
	
def cmd_addpeng(Message):
	Message.Chat.SendMessage('We\'re no strangers to love')
	time.sleep(0.5)	
	Message.Chat.SendMessage('You know the rules and so do I')
	time.sleep(0.5)	
	Message.Chat.SendMessage('A full commitment\'s what I\'m thinking of')
	time.sleep(0.5)	
	Message.Chat.SendMessage('You wouldn\'t get this from any other guy')
	time.sleep(0.5)
	Message.Chat.SendMessage('I just wanna tell you how I\'m feeling')
	time.sleep(0.5)
	Message.Chat.SendMessage('Gotta make you understand')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna give you up')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna let you down')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna run around and desert you')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna make you cry')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna say goodbye')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna tell a lie and hurt you')
	time.sleep(0.5)
	Message.Chat.SendMessage('We\'ve known each other for so long')
	time.sleep(0.5)
	Message.Chat.SendMessage('Your heart\'s been aching, but')
	time.sleep(0.5)
	Message.Chat.SendMessage('You\'re too shy to say it')
	time.sleep(0.5)
	Message.Chat.SendMessage('Inside, we both know what\'s been going on')
	time.sleep(0.5)
	Message.Chat.SendMessage('We know the game and we\'re gonna play it')
	time.sleep(0.5)
	Message.Chat.SendMessage('And if you ask me how I\'m feeling')
	time.sleep(0.5)
	Message.Chat.SendMessage('Don\'t tell me you\'re too blind to see')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna give you up')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna let you down')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna run around and desert you')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna make you cry')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna say goodbye')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna tell a lie and hurt you')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna give you up')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna let you down')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna run around and desert you')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna make you cry')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna say goodbye')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna tell a lie and hurt you')
	time.sleep(0.5)
	Message.Chat.SendMessage('(Ooh, give you up)')
	time.sleep(0.5)
	Message.Chat.SendMessage('(Ooh, give you up)')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna give, never gonna give')
	time.sleep(0.5)
	Message.Chat.SendMessage('(Give you up)')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna give, never gonna give')
	time.sleep(0.5)
	Message.Chat.SendMessage('(Give you up)')
	time.sleep(0.5)
	Message.Chat.SendMessage('We\'ve known each other for so long')
	time.sleep(0.5)
	Message.Chat.SendMessage('Your heart\'s been aching, but')
	time.sleep(0.5)
	Message.Chat.SendMessage('You\'re too shy to say it')
	time.sleep(0.5)
	Message.Chat.SendMessage('Inside, we both know what\'s been going on')
	time.sleep(0.5)
	Message.Chat.SendMessage('We know the game and we\'re gonna play it')
	time.sleep(0.5)
	Message.Chat.SendMessage('I just wanna tell you how I\'m feeling')
	time.sleep(0.5)
	Message.Chat.SendMessage('Gotta make you understand')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna give you up')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna let you down')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna run around and desert you')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna make you cry')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna say goodbye')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna tell a lie and hurt you')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna give you up')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna let you down')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna run around and desert you')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna make you cry')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna say goodbye')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna tell a lie and hurt you')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna give you up')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna let you down')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna run around and desert you')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna make you cry')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna say goodbye')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never gonna tell a lie and hurt you')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never Gonna Give You Up! (dance)')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never Gonna Let You Down! (dance)')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never Gonna Run Around and Desert You! (dance)')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never Gonna Make You Cry! (dance)')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never Gonna Say Goodbye! (dance)')
	time.sleep(0.5)
	Message.Chat.SendMessage('Never Gonna Tell A Lie! (dance)')
	time.sleep(0.5)
	Message.Chat.SendMessage('Or Hurt You! (dance)')
	time.sleep(0.5)
	print "Rick Command Received.\n"

def cmd_celebrate(Message):
	Message.Chat.SendMessage('Robot: Good job!')
	time.sleep(1)
	Message.Chat.SendMessage('Robot: You did great!')
	time.sleep(1)
	Message.Chat.SendMessage('Robot: Keep up the good work!')
	time.sleep(1)
	Message.Chat.SendMessage('Robot: (clap)')
	print "Celebrate Command Received.\n"
	    
def cmd_hammertime(Message):
	Message.Chat.SendMessage('Robot: EVERYONE!')
	time.sleep(1)
	Message.Chat.SendMessage('Robot: EVERYONE STOP WHAT YOU\'RE DOING!')
	time.sleep(1)
	Message.Chat.SendMessage('Robot: DO YOU GUYS EVEN KNOW WHAT TIME IT IS!?!?!?!?!?')
	time.sleep(1)
	Message.Chat.SendMessage('Robot: HAMMERTIME!!!!!!!! (dance)')
	print "Hammer time Command Received.\n"

def cmd_credit(Message):
	Message.Chat.SendMessage('Robot: Hi, I\'m Snayer\'s Bot.')
	Message.Chat.SendMessage('Robot: Everything on me was made by him.')
	Message.Chat.SendMessage('Robot: If you want to further develop me, just ask Snayer!')
	print "Credit Command Received.\n"

def cmd_help(Message):
	Message.Chat.SendMessage('Robot: Type !ping to see if the bot is alive!')
	Message.Chat.SendMessage('Robot: Type !celebrate to have a party!')
	Message.Chat.SendMessage('Robot: Type !rickroll to rick roll someone!')
	Message.Chat.SendMessage('Robot: Type !hammertime to stop, drop, and hammertime!')
	Message.Chat.SendMessage('Robot: Type !credit to see who made me!')
	Message.Chat.SendMessage('Robot: Type !spam for some yummy spam!')
	Message.Chat.SendMessage('Robot: Type !dice for a fun game!')
	print 'Help Command Recieved.\n'

def cmd_spam(Message):
	print 'Spam Command Recieved.\n'
	while True:
		Message.Chat.SendMessage('Robot: SPAM IS YUMMY!')

def cmd_intro(Message):
	Message.Chat.SendMessage('Robot: Hi!')
	time.sleep(2)
	Message.Chat.SendMessage('Robot: My name is Willis.')
	time.sleep(2)
	Message.Chat.SendMessage('Robot: Techincally, I\'m a robot!')
	time.sleep(2)
	Message.Chat.SendMessage('Robot: Type !help to see what I can do. :)')
	print "Introduce Command Received.\n"

def cmd_dice(Message):
	Message.Chat.SendMessage('Robot: Put a bet on numbers 1 through 6.')
	time.sleep(12)
	answer = random.randint(1,6)
	Message.Chat.SendMessage('Robot: *rolls dice*')
	time.sleep(1)
	Message.Chat.SendMessage('Robot: The dice rolled the number:') 
	Message.Chat.SendMessage(answer)
	print "Someone's playing dice. \n"

def cmd_goodjob(Message):
	Message.Chat.SendMessage("Robot: GOOD JOB M8!")
	Message.Chat.SendMessage("Robot: (clap)")
	Message.Chat.SendMessage("Robot: Keep up the good work!")
	print "Someone did a good job. \n"
	
def cmd_die(Message):	
	Message.Chat.SendMessage('Robot: Cya later faggots.')
	exit(0)

def cmd_party(Message):
	Message.Chat.SendMessage('Robot: YEAHHHHHHHHHHHH!!!')
	time.sleep(2)
	Message.Chat.SendMessage('Robot: PARTYYYYYYYYYYY!!!')
	Message.Chat.SendMessage('Robot: (party)')
	time.sleep(2)
	print "Party time. \n"

	
skype = Skype4Py.Skype(); 
skype.OnMessageStatus = commands 

if skype.Client.IsRunning == False: 
    skype.Client.Start() 
skype.Attach();

print 'Skype Bot currently running on user',skype.CurrentUserHandle, "\n"

while True: 
    raw_input('')