import random
from collections import Counter

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
  def calculate_score(dice_roll):
    #reset dice count and points
    points = 0
    dice_values = {
      6: 0,
      5: 0,
      4: 0,
      3: 0,
      2: 0,
      1: 0,
    }
    
    #count the dice
    for value in dice_roll:
      dice_values[value] += 1
      
    #check for straight
    # if all([count == 1 for count in dice_values.values()]):
    #   return 1500

    #check for straight
    temp = Counter(dice_roll)
    print(temp)
    print(len(temp))
    if len(temp) == 6:
      return 1500

    #check for pairs
    pair_count = 0
    for count in dice_values:
      if dice_values[count] == 2:
        pair_count += 1
    if pair_count == 3:
      return 1500

    #generic matches
    for count in dice_values:
      if count != 1 and dice_values[count] > 2:
        points += count * 100 * (dice_values[count] - 2)
      elif count == 1:
        if dice_values[count] < 3:
          points += 100 * dice_values[count]
        else:
          points += 1000 * (dice_values[count]-2)
      elif count == 5:
        points += 50 * dice_values[count]
    return points


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