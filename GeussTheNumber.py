# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui


# initialize global variables used in your code
random_number = 0
number_guesses = 0
max_number = 0


# helper function to start and restart the game
def new_game():
    global random_number
    global max_number
    global number_guesses
    
    number_guesses = 7
    max_number = 100
    
    random_number = random.randrange (0,100)
    
    
    
    print "New Game.  Range is from 0 to " + str(max_number)
    print "You have " + str(number_guesses) + " guesses remaining"

    return random_number

# define event handlers for control panel
def range_100():
    # button that changes range to range [0,100) and restarts
    global random_number
    global max_number
    global number_guesses

    number_guesses = 7
    max_number = 100
    random_number = random.randrange(0,100)
    
    
    print "                            "
    print "New Game.  Range is from 0 to " + str(max_number)
    print "You have " + str(number_guesses) + " guesses remaining"
    
    return random_number
    
def range_1000():
    # button that changes range to range [0,1000) and restarts
    global random_number
    global max_number
    global number_guesses
    
    number_guesses = 10
    max_number = 1000
    
    random_number = random.randrange(0,1000)
    
    
    print "                             "
    print "New Game.  Range is from 0 to " + str(max_number)
    print "You have " + str(number_guesses) + " remaining"
    
    return random_number
    
def input_guess(guess):
    # main game logic goes here	
    global number_guesses
    
    
    
    if guess.isdigit() == True:
        
    
    #checks to determine player is inputing a guess between the min and max
        if int(guess) != random_number and number_guesses < 1:
            
            print "                        "
            print "Guess was " + str(guess)
            print "Number of guesses remaining " + str(number_guesses)
            print "You ran out of guesses.  The number was " + str(random_number)
            
        elif int(guess) > random_number and number_guesses > 0:
            
            print "                             "
            print "Guess was " + str(guess)
            print "Number of guesses remaining " + str(number_guesses)
            print "Lower!"
            
            number_guesses -= 1
            
        elif int(guess) < random_number and number_guesses > 0:
            
            print "                           "
            print "Guess was " + str(guess)
            print "Number of guesses remaining " + str(number_guesses)
            print "Higher!"
            
            number_guesses -= 1
            
        elif int(guess) == random_number and number_guesses > 0:
            
            print "                          "
            print "Guess was " + str(guess)
            print "Number of guesses remaining " + str(number_guesses)
            print "Correct!"
           
        else:
            "Please input another number"
            
    #prints an error message if player guess is outside the range
    
    else:
        print "Please input a number"
    
# create frame
frame = simplegui.create_frame("Geuss The Number", 200, 200)


# register event handlers for control elements
frame.add_button("Range from 0 to 100", range_100 , 200)
frame.add_button("Range from 0 to 1000", range_1000, 200)
frame.add_input("Enter a Geuss", input_guess, 100)


# call new_game and start frame 
frame.start()
new_game()

 
#always remember to check your completed program against the grading rubric
