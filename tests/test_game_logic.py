import pytest
from game_of_greed.game_logic import GameLogic

def test_roll_dice_6():
    actual = len(GameLogic.roll_dice(6))
    expected = 6
    assert actual == expected

def test_roll_dice_4():
    actual = len(GameLogic.roll_dice(4))
    expected = 4
    assert actual == expected

def test_roll_dice_2():
    actual = len(GameLogic.roll_dice(2))
    expected = 2
    assert actual == expected

def test_roll_dice_1():
    actual = len(GameLogic.roll_dice(1))
    expected = 1
    assert actual == expected

def test_roll_dice_6_ints():
    actual = True
    for die in GameLogic.roll_dice(6):
      if die > 6 or die < 1:
        actual = False
    expected = True
    assert actual == expected

def test_roll_dice_4_ints():
    actual = True
    for die in GameLogic.roll_dice(4):
      if die > 6 or die < 1:
        actual = False
    expected = True
    assert actual == expected
