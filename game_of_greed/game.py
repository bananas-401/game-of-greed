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
        while self.banker.balance < 10000 and self.round_num < self.num_rounds:
            self.round_num += 1
            self.start_round()

    def start_round(self):
        cheater = False
        dice = 6
        response = 'l'

        print(f'Starting round {self.round_num}')

        while response != 'q':
            roll_result = self._roller(dice)
            print(f'Rolling {dice} dice...')
            valid = False
            while not valid:
                print("*** " +" ".join([str(i) for i in roll_result]) + " ***")

                #check for zilch
                roll_score = GameLogic.calculate_score(roll_result)
                if roll_score == 0:
                    self.zilch()
                    return
            
                print('Enter dice to keep, or (q)uit:')
                response = input('> ')
                #check for quit
                if response == 'q':
                    self.quit_game()
                #calculate kept dice score, how many dice were kept/remaining, prompt to roll, quit or bank again
                # else:
                scores_tuple = GameLogic.get_scorers(roll_result)
                keepers = [int(x) for x in response if x.isdigit()]
                valid = GameLogic.validate_keepers(scores_tuple, keepers)

            number_of_dice_banked = len(keepers)
            roll_score = GameLogic.calculate_score(keepers)
            self.banker.shelf(roll_score)
            dice = len(roll_result) - len(keepers)
            print(f'You have {self.banker.shelved} unbanked points and {dice} dice remaining')
            print('(r)oll again, (b)ank your points or (q)uit:')
            if dice == 0:
                dice = 6

            response = input('> ')
            if response == 'q':
                self.quit_game()

            elif response == 'b':
                amount_deposited = self.banker.bank()
                print(f'You banked {amount_deposited} points in round {self.round_num}')
                print(f'Total score is {self.banker.balance} points')
                return

    def zilch(self):
        print('****************************************')
        print('**        Zilch!!! Round over         **')
        print('****************************************')
        print(f'You banked 0 points in round {self.round_num}')
        print(f'Total score is {self.banker.balance} points')

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

