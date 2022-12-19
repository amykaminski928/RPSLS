from player import Player
import random
class AI(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def choose_gesture(self):
        #self.ai_choice= random(self.gestures)
        #print(f"Your opponent has chosen {random(self.gestures)}")