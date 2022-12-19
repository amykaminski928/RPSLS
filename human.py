from player import Player
class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        index=0
        for gesture in self.gestures:
            self.choice=input(f'Choose {index} for {gesture}')
            index+=1
            