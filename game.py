from human import Human
from ai import AI
import interface as ui 

class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        
    def run(self):
        self.game_type()
        self.player_turn()
        
    def game_type(self):
        #the """ words """ characters allow you to create a list or other strings in a block as one string
        self.user_selection=ui.validate_to_int("""
        Please select from the options below:
        Press 1 for Human v. Human
        Press 2 for Human v. AI
        Press 3 for AI v. AI
        """)
        if self.user_selection == "1":
            self.player_one= Human("Player 1")
            self.player_two= Human("Player 2")
        if self.user_selection == "2":
            self.player_one= Human("Player 1")
            self.player_two= AI("Player 2")
        if self.user_selection == "3":
            self.player_one= AI("Player 1")
            self.player_two= AI("Player 2")
        
    def player_turn(self):
        #need to have choose gesture called here for both players
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        print(f"""{self.player_one} chose {self.player_one.choice}.
        {self.player_two} chose {self.player_two.choice}.""")
        
    def winner_check(self):
        #need to add rules/hierarchy of winning moves here as while loop?
        pass

    def compare_gests(self):
        if self.player_one.choice==self.player_two.choice:
            print("Tie")
        elif self.player_one.choice==self.player_one.choice[0] and (self.player_two.choice==self.player_two.choice[1] or [3]):
            self.player_one.score+=1
        elif self.player_one.choice==self.player_one.choice[1] and (self.player_two.choice==self.player_two.choice[2] or [3]):
            self.player_one.score+=1
        elif self.player_one.choice==self.player_one.choice[2] and (self.player_two.choice==self.player_two.choice[0] or [4]):
            self.player_one.score+=1
        elif self.player_one.choice==self.player_one.choice[3] and (self.player_two.choice==self.player_two.choice[2] or [4]):
            self.player_one.score+=1
        elif self.player_one.choice==self.player_one.choice[4] and (self.player_two.choice==self.player_two.choice[0] or [1]):
            self.player_one.score+=1
        elif self.player_one.choice==self.player_one.choice[0] and (self.player_two.choice==self.player_two.choice[2] or [4]):
            self.player_two.score+=1
        elif self.player_one.choice==self.player_one.choice[1] and (self.player_two.choice==self.player_two.choice[0] or [4]):
            self.player_two.score+=1
        elif self.player_one.choice==self.player_one.choice[2] and (self.player_two.choice==self.player_two.choice[1] or [3]):
            self.player_two.score+=1
        elif self.player_one.choice==self.player_one.choice[3] and (self.player_two.choice==self.player_two.choice[0] or [1]):
            self.player_two.score+=1
        elif self.player_one.choice==self.player_one.choice[4] and (self.player_two.choice==self.player_two.choice[2] or [3]):
            self.player_two.score+=1
          