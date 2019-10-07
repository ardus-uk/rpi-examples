#!/usr/bin/python3

# Guess The Number
# Peter Normington 2019-10-06
# Mark Bradley 2019-10-07  Testing Github no changes made to code.

from random import randint

class NumberGenie:
    def __init__(self):
        self.secret = randint(0,9)
        self.max_guesses = 5
        self.success_message = "Well done!"
        self.failure_message = "Hard luck!"

    def prompt(self):
        print("I'm open for business...")
        print("I'm thinking of a number in the range 0 to 9...")

    def play(self):
        guess_count = 0
        success = False
        while guess_count < self.max_guesses and not success:
            guess = int(input("What's your guess? > "))
            guess_count += 1
            if guess == self.secret:
                success = True
            else:
                if guess > self.secret:
                    print("That was too high")
                else:
                    print("That was too low")
        if success:
            print(self.success_message)
        else:
            print(self.failure_message)


ng = NumberGenie()
ng.prompt()
ng.play()

    
    
    