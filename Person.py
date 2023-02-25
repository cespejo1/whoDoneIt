#This class will represent the character the user will be. We will add attributes 
# here that we want the user to have and change throughout the game



class Person:
  def __init__(self, name, health):
    self.name = name
    self.health = health

# getter method
  def get_health(self):
      return self.h
      
# setter method
  def set_health(self, x):
      self.health = x

  def reduce_health(self, x):
      self.health = self.health - x

  def add_health(self, x):
      self.health = self.health + x

