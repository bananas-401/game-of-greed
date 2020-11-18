from game_logic import GameLogic, Banker


class Game:
    """Class for Game of Greed application
    """

    def __init__(self, num_rounds=20):
        self.banker = Banker()
        self.num_rounds = num_rounds

    def play(self, roller=None):
        """Entry point for playing (or declining) a game

        Args:
            roller (function, optional): Allows passing in a custom dice roller function.
                Defaults to None.
        """

        self.round_num = 0

        self._roller = roller or GameLogic.roll_dice

        print("Welcome to Game of Greed")

        print("(y)es to play or (n)o to decline")

        response = input("> ")

        if response == "y" or response == "yes":
            self.start_game()
        else:
            self.decline_game()

    def decline_game(self):
        print("OK. Maybe another time")

    def start_game(self):
        dice = 6

        while Banker.bank != 10000:

            response = input("Type 'r' to roll your dice! > ")
            if response == "r":
                roll_result = GameLogic.roll_dice(dice)
                print('*rolling*')
                print(f"Your roll is: {roll_result}")
            else:
                print('type r please')

            response = input("Would you like to stash any dice?  y/n > ")
            if response == "y":
                response = input("type the dice numbers with no separating commas or spaces > ")
                    roll_result
            elif response == "n":
                response = ('passing turn')
            else:
                break

            
            

        


if __name__ == "__main__":
    game = Game()
    game.play()
