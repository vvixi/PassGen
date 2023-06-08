# Password and string generator in Python 3.10 by vvixi
import random
import string
import os
import time

def makePassword(length, num=False, strength='weak') -> str:
	'''length of password, num if you want a number,
    and strenth: weak, medium, strong'''
	lower = string.ascii_lowercase
	upper = string.ascii_uppercase
	dig = string.digits
	letter = lower + upper
	punct = string.punctuation
	pwd = ''

	if strength == 'weak':
		if num:
			length -= 2
			for i in range(2):
				pwd += random.choice(dig)
		for i in range(length):
			pwd += random.choice(lower)

	elif strength == 'medium':
		if num:
			length -= 2
			for i in range(2):
				pwd += random.choice(dig)
		for i in range(length):
			pwd += random.choice(letter)

	elif strength == 'strong':
		ran = random.randint(4, 7)
		if num:
			length -= ran
			for i in range(ran):
				pwd += random.choice(dig)
		length -= ran
		for i in range(ran):
			pwd += random.choice(punct)
		for i in range(length):
			pwd += random.choice(letter)

	pwd = list(pwd)
	random.shuffle(pwd)
	return ''.join(pwd)

def displayPassword():

    print(makePassword(15,num=True))
    print(makePassword(20,num=True, strength="medium"))
    print(makePassword(29, strength="strong"))
    time.sleep(8)
    os.system('cls' if os.name == 'nt' else 'clear')

answer = input("Make password? ")
if answer == 'yes' or answer == 'YES' or answer == 'Yes':
    displayPassword()
