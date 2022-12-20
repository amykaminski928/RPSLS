from human import Human
from ai import AI
import interface as ui 

class Game:
    def __init__(self):
        self.player_one = ("test")
        self.player_two = ("test")
        pass

    def run(self):
        self.game_type()
        self.victory_message(self.winner_check)
        pass

    def game_type(self):
        #the """ words """ characters allow you to create a list or other strings in a block as one string
        self.user_selection=ui.validate_to_int("""
        Please select from the options below:
        Press 1 for Human v. Human
        Press 2 for Human v. AI
        Press 3 for AI v. AI
        """)
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
        #need to have choose gesture called here for both players
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        print(f"{self.player_one} chose {self.player_one.choice}.  {self.player_two} chose {self.player_two.choice}.")
        self.compare_gests()
        pass
        
    def winner_check(self):
        while self.player_one.score<3 and self.player_two.score<3:
            self.player_turn()
        if self.player_one.score>=3:
            return self.player_one
        return self.player_two
        pass
        
    def compare_gests(self):
        if self.player_one.choice==self.player_two.choice:
            print("Tie")
        elif self.player_one.choice==self.player_one.choice[0]:
            self.round_recap(1,3)
        elif self.player_one.choice==self.player_one.choice[1]:
            self.round_recap(2,3)
        elif self.player_one.choice==self.player_one.choice[2]:
            self.round_recap(0,4)
        elif self.player_one.choice==self.player_one.choice[3]:
            self.round_recap(2,4)
        elif self.player_one.choice==self.player_one.choice[4]:
            self.round_recap(0,1)
        pass

    def round_recap(self, int_1, int_2):
        if (self.player_two.choice==self.player_two.choice[int_1] or self.player_two.choice==self.player_two.choice[int_2]):
            self.player_one.score+=1
            print(f"{self.player_one.name} wins this round.")
        else: self.player_two.score+=1
        print(f"{self.player_two.name} wins this round.")
        print(f"The score is now {self.player_one.name} with {self.player_one.score} to {self.player_two.name} with {self.player_two.score} points.")
        pass

    def victory_message(self, obj):
        print(f"{obj.name} is the winner!")
        pass