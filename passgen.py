# Password and string generator in Python 3.10 by vvixi
import random
import string
import os
import time
from argparse import ArgumentParser

def makePassword(length=10, num=False, strength='weak'):
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
			length -= 4
			for i in range(4):
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
	password = ''.join(pwd)
	print("Success")
	return password

def displayPassword(_length, _num, _strength):
    
    while int(_length) < 6:
        choice = input("Please chose a number greater than 5: ")
        _length = choice

    password = makePassword(int(_length), _num, _strength)
    answer = input("Display password? ")

    if answer == 'yes' or answer == 'YES' or answer == 'Yes':
        
        print(password)
        time.sleep(8)
        os.system('cls' if os.name == 'nt' else 'clear')

    elif answer == 'no' or answer == 'NO' or answer == 'No':
        print("Thank you for using PassGen")
        return

if __name__ == '__main__':
    # create the argparse instance
    parser = ArgumentParser(
                prog = 'PassGen',
                description = 'Easily create complex strings and passwords')
    parser.add_argument("-l", "--length", dest="length", help="length of password")
    
    parser.add_argument("-n", "--numbers", dest="num", help="contains numbers")

    parser.add_argument("-s", "--strength", dest="strength", help="specify strength of password")

    args = parser.parse_args()

    displayPassword(args.length, args.num, args.strength)
