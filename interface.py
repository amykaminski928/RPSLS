#learned this from video from Pascal: able to create a function that will check the user input at any level of the game.
def validate_to_int(str_input):
    while True:
        try:
            user_input=input(str_input)
            return int(str_input)

        except:
            print ("Sorry that was not an integer.")