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
print("Enjoy the journey, ", userName, "!\n\n")
print("If at anytime you would like to quit the game, enter q or Q or quit when asked for input.\n\n Otherwise type start to begin your adventure.\n\n\n")

# This will be the Game loop.
while gameIsOver == False:
    userInput = input("What would you like to do? ")
    if (userInput == "q" or userInput == "Q" or userInput == "quit"):
        gameIsOver = True
        delprint("Thanks for playing!")

    elif (userInput == "start" or userInput == "Start"):
        delprint("\n\n\nAnd so we begin our tale...\n \n \n")
        delprint(
            f"The frigid rain pelts {userName}'s neck and back as he forces \nhimself to take another weary step through the sludge.\n\n")
        delprint("\x1B[3mWhat's that up ahead?\x1B[0m, he thinks\n")
        delprint(
            f"Barely visible through the downpour, {userName} can just make out a dark shape rising from the mud.\n\n")
        delprint(
            f"Relief washes over him as he realizes what it is.\n\n \x1B[3mA signpost!\x1B[0m\n\n")

        userInput = input("What do you want to do?")

        if (userInput == "approach the signpost" or userInput == "read the signpost" or userInput == "approach" or userInput == "read"):
            delprint(
                "Despite being worn down by wind and time, the letters on the sign are still legible: \x1B[3m<Insert ool and creepy town name here>\x1B[0m\n\n\n")
        else:
            delprint(
                "That doesn't seem to be an option right now. Try something else.")
