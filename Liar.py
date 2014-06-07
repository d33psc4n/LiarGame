# I need to fill those
# How many do i neeed really
# I saw quite a few at some people  
# I will put 5 at least.
# Yeah 5 is good
# Shit last one was 5... 6 be it then.
import glob
import random
import time
import subprocess
import sys
import os
os.system("clear")
print '                   Very Fun Game' 
print '.____    .__                 ________                       '
print'|    |   |__|____ _______   /  _____/_____    _____   ____  '
print'|    |   |  \__  \\_  __ \ /   \  ___\__  \  /     \_/ __ \ '
print'|    |___|  |/ __ \|  | \/ \    \_\  \/ __ \|  Y Y  \  ___/ '
print'|_______ \__(____  /__|     \______  (____  /__|_|  /\___  >'
print'        \/       \/                \/     \/      \/     \/  '
print'd33p_sc4n wrote the code :D' #A.k.a. cel mai talentat :)))))
time.sleep(2)
os.system("clear")

os.chdir("Poze")

count1C = 0
count1I = 0
count2C = 0
count2I = 0 
def Player1():
	global count2C
	global count2I
	def Check():
		global count1C
		global count1I
		answer = raw_input("Did he give a correct answer?(y/n)\n> ")
		if answer == "y":
			count1C += 1 
		elif answer == "n":
			count1I += 1
		else:
			Check()
		os.system("clear")
            
	def Choose():
		global rounds
		global timer
		pics = [i for i in glob.glob("*.jpg")]
		random.shuffle(pics)
		random.shuffle(pics)
		choice = random.choice(pics)
		process = subprocess.Popen([displayer,choice])
		time.sleep(timer)
		process.kill()
	for i in range(0,rounds):
		Choose()
		Check()
	if count2C == 0 and count2I == 0:
		print "Player2's turn now! Switchhhh. "
		time.sleep(4)
		os.system("clear")

def Player2():
	global count1C
	global count1I
	def Check():
		global count2C
		global count2I
		answer = raw_input("Did he give a correct answer?(y/n)\n> ")
		if answer == "y":
			count2C += 1 
		elif answer == "n":
			count2I += 1
		else:
			Check()
		os.system("clear")
            
	def Choose():
		global rounds
		global timer2
		pics = [i for i in glob.glob("*.jpg")]
		choice = random.choice(pics)
		process = subprocess.Popen([displayer,choice])
		time.sleep(timer2)
		process.kill()
	for i in range(0,rounds):
		Choose()
		Check()
	if count1C == 0 and count1I == 0:
		print "Player1's turn now! Switchhhh. "
		time.sleep(5)
		os.system("clear")


os.system("clear")
displayer = raw_input("Choose your image displayer(ex: shotwell, display) or just leave blank for default.\n> ")
os.system("clear")
if displayer == "":
	displayer = "display"
elif displayer == "s":
	displayer = "shotwell"
helper = raw_input("Do you want to view the game rules?(y/n)\n> ")
if helper == "y":
	os.chdir("..")
	txtviewer2 = raw_input("Choose your text viewer(Leave blank for nano):\n>  ")
	if txtviewer2 == "":
		txtviewer2 = "nano" 
	helping = subprocess.Popen([txtviewer2, "inst.txt"])
	helping.wait()
	os.chdir("Poze")
os.system("clear")
rounds = raw_input("How many rounds are you going to play?\n> ")
rounds = int(rounds)
os.system("clear")
player = raw_input("Are you evaluating player 1 or 2?\n> ")
os.system("clear")
if player == "1":
	timer = raw_input("Set time to view images:\n> ")
	timer = int(timer)
	os.system("clear")
	Player1()
	timer2 = raw_input("Set time to view images:\n> ")
	timer2 = int(timer2)
	os.system("clear")
	Player2()
elif player == "2":
	timer2 = raw_input("Set time to view images:\n> ")
	timer2 = int(timer2)
	os.system("clear")
	Player2();
	timer = raw_input("Set time to view images: \n> ")
	timer = int(timer)
	os.system("clear")
	Player1()
else:
	print "Please try again!"

time.sleep(1)
os.system("clear")
    
print "Time is up ! Game is over. Here are your results:" 
os.chdir("..")
file = open('results.txt' ,'w')
file.write("Correct answers Player1: %s" % count1C)
file.write("\n")
file.write("Incorrect answers Player1: %s" % count1I)
file.write("\n")
file.write("\n")
file.write("Correct answers Player2: %s" % count2C)
file.write("\n")
file.write("Incorrect answers Player2: %s" % count2I)
file.write("\n")
file.write("\n")
if count1C > count2C:
	file.write("Winner: Player1 . Congratz Player1!")
elif count1C == count2C:
	file.write("Winner: Nobody won! Equality FTW")
else:
	file.write("Winner: Player2. Congratz Player2!")
file.close();
os.system("clear")
txtviewer = raw_input("Choose your text viewer(Leave blank for nano):\n>  ")
if txtviewer == "":
	txtviewer = "nano"  
os.system("clear")
results = subprocess.Popen([txtviewer,"results.txt"])
results.wait()



    



