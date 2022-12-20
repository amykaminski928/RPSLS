from player import Player
import interface as ui 
class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
            
        self.user_selection=ui.validate_to_int(f"""
Please select from the options below:
Choose 1 for {self.gestures[0]}  
Choose 2 for {self.gestures[1]}
Choose 3 for {self.gestures[2]}
Choose 4 for {self.gestures[3]}
Choose 5 for {self.gestures[4]}""") 
        self.current_gesture=self.gestures[self.user_selection-1]
        self.current_gesture=int

            