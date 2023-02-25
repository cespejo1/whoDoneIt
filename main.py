from Person import Person
# print("this will be bigger than 💥 Call of Duty 💥")

#This class will be the class that will load the game and run the game.
#The game will have a loop which will keep the game running. I'm thinking
#we build the game from the ground up and make the game start off simple and 
#we slowly add more and more.

#initial setup
p1 = Person("John", 36)


#This will be the Game loop. 
gameIsOver = False
userName = input("Welcome to the greatest game you'll ever play. To start off, what is the name of your character?\n")

print("Enjoy the journey, ", userName, "!")
print("If at anytime you would like to quit the game, enter q or Q or quit when asked for input")

while gameIsOver == False:
  userInput = input("What would you like to do?")
  if(userInput == "q" or userInput == "Q" or userInput == "quit"):
    gameIsOver = True
    print("Thanks for playing!")




