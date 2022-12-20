#learned this from video from Pascal: able to create a function that will check the user input at any level of the game.
def validate_to_int(str_input):
    while True:
        try:
            user_input=input(str_input)
            return int(user_input)
            
        except:
            print ("Sorry that was not an integer.")
#Want to create a function that will let user know what each player chose and who winner was in round? no, would like to add to game file
#print(f"{self.player_one.name} wins this round.")
#print(f"{self.player_two.name} wins this round.")
#print(f"The score is now {self.player_one.name} with {self.player_one.score} to {self.player_two.name} with {self.player_two.score} points.")
