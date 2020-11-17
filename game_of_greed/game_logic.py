import random

active_game = True

class GameLogic:  
  def __init__(self):
    pass

  @staticmethod
  def roll_dice(number_of_dice):
    result = []
    for die in range(number_of_dice):
      result.append(random.randint(1,6))
    return tuple(result)

  @staticmethod
  def calculate_score(tuple_input):
    return 42


class Banker:
  def __init__(self):
    pass

  def shelf():
    pass

  def Bank():
    pass

  def clear_shelf():
    pass

current_roll = GameLogic.roll_dice(6)
print(current_roll)

current_score = GameLogic.calculate_score(current_roll)
print(current_score)