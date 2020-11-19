import sys

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
        #todo make dice count dynamic
        self.start_round()

    def start_round(self):
        dice = 6

        while self.banker.balance < 10000 and self.round_num < self.num_rounds:
            self.round_num += 1

            roll_result = self._roller(dice)
            print(f'Starting round {self.round_num}')
            print(f'Rolling {dice} dice...')
            print("*** " +" ".join([str(i) for i in roll_result]) + " ***")
            print('Enter dice to keep, or (q)uit:')
            
            response = input('> ')
            if response == 'q':
                self.quit_game()
            elif response == '5':
                print('You have 50 unbanked points and 5 dice remaining')
                print('(r)oll again, (b)ank your points or (q)uit:')

            response = input('> ')
            if response == 'b':
                print('You banked 50 points in round 1')
                print('Total score is 50 points')

    def quit_game(self):
        bank_ = self.banker.balance
        print(f'Thanks for playing. You earned {bank_} points')


        sys.exit()



if __name__ == "__main__":
    from game_logic import GameLogic, Banker
    game = Game()
    game.play()
else:
    from game_of_greed.game_logic import GameLogic, Banker
