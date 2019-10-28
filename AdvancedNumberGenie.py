#!/usr/bin/python3

# Guess The Number
# Peter Normington 2019-10-06
# Mark Bradley 2019-10-07
# Modified to allow passing of parameters to set number range and guesses

from random import randint

class AdvancedNumberGenie:
    def __init__(self,low,high,goes):
        self.secret = randint(low,high)
        self.low = low
        self.high = high
        self.max_guesses = goes
        self.success_message = "Well done!"
        self.failure_message = "Hard luck!"

    def prompt(self):
        print("I'm open for business...")
        print("I'm thinking of a number in the range ",self.low," to ",self.high,"...")

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
            print(self.failure_message," It was ",self.secret)


# Test the class
if __name__ == '__main__':
    ng = AdvancedNumberGenie(1,100,7)
    ng.prompt()
    ng.play()

    
    
    