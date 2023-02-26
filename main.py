from Person import Person
import sys
import time

# don't know if this is more hassle than it's worth but it's kind of fun


def delprint(text, delay_time=.05):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay_time)


# This class will be the class that will load the game and run the game.
# The game will have a loop which will keep the game running. I'm thinking
# we build the game from the ground up and make the game start off simple and
# we slowly add more and more.

# initial setup
p1 = Person("John", 36)
gameIsOver = False


userName = input(
    "Welcome to the greatest game you'll ever play. To start off, what is the name of your character?\n")
print("Enjoy the journey, ", userName, "!")
print("If at anytime you would like to quit the game, enter q or Q or quit when asked for input, otherwise type start to begin your adventure.")

# This will be the Game loop.
while gameIsOver == False:
    userInput = input("What would you like to do? ")
    if (userInput == "q" or userInput == "Q" or userInput == "quit"):
        gameIsOver = True
        delprint("Thanks for playing!")

    elif (userInput == "start" or userInput == "Start"):
        delprint("And so we begin our tale...", .05)
