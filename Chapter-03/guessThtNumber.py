#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


secretNumber = random.randint(1, 1000)
print('I am thinking of a num between 1, 1000 ')
guessT = True
count = 0
while guessT:
    print('Take a guess.')
    guess = int(input())
    count += 1
    if count < 20:
        if guess < secretNumber:
            print('you guess is too low')
        elif guess > secretNumber:
            print('your guess is too high')
        else:
            guessT = False
            print('Good job! You guessed my number in ' + str(guess) + ' guesses!')
            break
    else:
        print('次数用完')
        guessT
        print('the number is ',str(guess))
        break

