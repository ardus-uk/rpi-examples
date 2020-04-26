#!/usr/bin/python3

def article(name):
    if name[0] in ('a','e','i','o','u'):
        return "an"
    else:
        return "a"

def single_or_plural(simpleword,number):
# This is to pluralise words, simply by adding the letter "s".
# It's not going to work for a sheep, a goose, or a fly
# but at least we'd hope that they aren't in the fruit bowl.
# However, watch out for the mango...
    if number == 1: 
        return simpleword
    else:
        return simpleword + 's'


class FruitBowl:

    def __init__(self):
        print("Mmm...a new, empty fruit bowl.")
        self.bowl = {}

    def add_single(self,fruit):
        if fruit in self.bowl:
            self.bowl[fruit] = self.bowl[fruit] + 1
        else:
            self.bowl[fruit] = 1
        print("That's " + article(fruit) + " " + fruit + " added to the bowl")

    def add_multiple(self,fruit,number):
        if fruit in self.bowl:
            self.bowl[fruit] = self.bowl[fruit] + number
        else:
            self.bowl[fruit] = number
        print("There are " + str(number) + " " + single_or_plural(fruit,number) + " added to the bowl")

    def take_item(self,fruit):
        if fruit in self.bowl:
            self.bowl[fruit] = self.bowl[fruit] - 1
            print("That's " + article(fruit) + " " + fruit + " taken out of the bowl.")
            if self.bowl[fruit] == 0:
                del self.bowl[fruit]
        else:
            print("There aren't any " + fruit + "s in the bowl!")


    
    def show_contents(self):
        if self.bowl:
            print("The contents of the fruit bowl are:")
            for fruit in sorted(self.bowl.keys()):
                number = self.bowl[fruit]
                print("\t",number,single_or_plural(fruit,number))
        else:
            print("Nothing in the bowl!")

# Test the class
if __name__ == '__main__':
    fb = FruitBowl()
    fb.show_contents()
    fb.add_single("orange")
    fb.show_contents()
    fb.add_single("banana")
    fb.show_contents()
    fb.add_multiple("lemon",4)
    fb.show_contents()
    fb.add_multiple("grape", 300)
    fb.show_contents()
    fb.take_item("lemon")
    fb.show_contents()
    fb.take_item("orange")
    fb.show_contents()
    fb.take_item("orange")
    fb.show_contents()
    fb.add_single("python")
    fb.show_contents()
    fb.add_single("python")
    fb.show_contents()
   