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
    #if len(Counter(dice_roll)) == 6 and dice_values.values() == 1 returns 150... why...
    if len(Counter(dice_roll)) == 6:
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

  @staticmethod
  def get_scorers(value_of_rolled_dice):
    #input is going to a list/tuple of varied lengths containing intengers of each dice rolled
    #output will be a list of dice that contributed to the score.
    score_using_all_dice = GameLogic.calculate_score(value_of_rolled_dice)

    if score_using_all_dice == 0:
      return tuple()

    scoring_dice = []

    for die in range(len(value_of_rolled_dice)):
      sub_roll = value_of_rolled_dice[:die] + value_of_rolled_dice[die + 1:]
      sub_score = GameLogic.calculate_score(sub_roll)

      if sub_score != score_using_all_dice:
        scoring_dice.append(value_of_rolled_dice[die])

    return tuple(scoring_dice)

  @staticmethod
  def validate_keepers(scores_tuple, keepers):
    rolled_scoring_dice = list(scores_tuple)
    for value in keepers:
      if value not in rolled_scoring_dice:
        print('Cheater!!! Or possibly made a typo...')
        return False
      else:
        rolled_scoring_dice.remove(value)
    return True


class Banker:
  def __init__(self):
    self.balance = 0
    self.shelved = 0

  def shelf(self, amt):
    self.shelved += amt

  def bank(self):
    amount_deposited = self.shelved
    self.balance += self.shelved
    self.shelved = 0
    return amount_deposited

  def clear_shelf(self):
    self.shelved = 0

# current_roll = GameLogic.roll_dice(6)
# print(current_roll)

# current_score = GameLogic.calculate_score(current_roll)
# print(current_score)