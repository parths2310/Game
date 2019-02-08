#!/usr/bin/env python3

import random

number= random.randint(1,10)

tries = 1



question = input("would you like to play a game? [y/n]")
if question == 'n':
	print("oh.nice")

if question =='y':
	print("I'm thinking of a number between 1 & 10")
	
	gu = int(input("have a guess:"))
	
	if gu > number:
		print ("Guess Lower...")

if gu < number :
		print("Guess Higher")

while gu != number :
	tries +=1
	gu=int(input("Try again.."))
	if gu < number :
		print("Guess Higher")

if gu == number :
	print("you're a genius, the number was", number, \
		"and it only", tries,"tries!")

