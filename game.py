from human import Human
from ai import AI
import interface as ui 

class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        pass
    def run(self):
        self.game_type()
        pass
    def game_type(self):
        #the """ words """ characters allow you to create a list or other strings in a block as one string
        self.user_selection=ui.validate_to_int("""
        Please select from the options below:
        Press 1 for Human v. Human
        Press 2 for Human v. AI
        Press 3 for AI v. AI""")
        if self.user_selection == 1:
            self.player_one= Human("Player 1")
            self.player_two= Human("Player 2")
        if self.user_selection == 2:
            self.player_one= Human("Player 1")
            self.player_two= AI("Player 2")
        if self.user_selection == 3:
            self.player_one= AI("Player 1")
            self.player_two= AI("Player 2")
        pass
    def player_turn(self):
        pass
    def winner_check(self):
        pass