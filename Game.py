from sys import exit
from sys import argv



#Item variables not used for future developement 
rock = 2
sword = 5
stick = 2
shield = 25
axe = 9
bow = 10
arrow = 4
torch = 3

def intro():
    print "You are in a forest lush with green tree's"
    print "In front of you is a castle with a iron gate."
    print "Do you 'open the gate' or 'walk in the opposite direction'?"
    
def front_gate():
    castlegate = raw_input("> ")

    if castlegate == "open the gate":
        court_yard()
    elif castlegate == "walk in the opposite direction":
        dead("You start walking into a forest. You stumble and fall of a cliff.")
    elif castlegate <= "open the gate":
        dead (" You did not follow the rules... Sorry")
    else:
        front_gate()

# end game for the user 	
def dead(death):
	print death, "Game Over!"
	exit(0)
    
def court_yard():
        print "You are in a court yard trees everywhere."
        print "You see a red, green, and blue door. Which door do you open?"
        door = raw_input("> ")
        if door == "red":
            red_door()
        elif door == "green":
		    green_door()
        elif door == "blue":
		    blue_door()
        else: 
            print "You walk back to the forest and fall asleep under a tree."
            intro()
            front_gate()

def green_door():
   print  "As you get closer to the door hums.... Strange...."
   print  "The door says please pick a number 1 through 10."
   print  "What number do you choose?"
       #door_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   guessnumber = input ("> ")    
   if guessnumber <= 5:
       print "You are allowed to enter."
       print "The door opens slowly for you."
       dead("To be continued.")
   elif guessnumber >= 6:
	   print "You are not allowed to enter." 
	   print "Nothing else happens......."
	   court_yard()
   elif guessnumber >10:
      dead("You did not listen to the rules. You are sucked into a worm hole never to be seen again. ")
   else:
      dead("What in the world did you guess??")

def red_door():
	print "The door is locked. You need a key to unlock it."
	court_yard()
	

def blue_door():
    print  "The door opens slowly, to room filled with gold coins."
    print  "How many coins do you take ?"
    pockets = input ("> ")
    if pockets <= 500:
        print "You place a handful of coins in your pocket."
        print "You quickly shut the door before anyone sees you."
        print "You run outside the gate it slams closed behind you."
        intro()
        front_gate()
    elif pockets > 500:
       print "As you are filling your pockets with gold something moves."
       print "Suddenly a snack leaps out from under the coins bitting you."
       dead("Everything goes dark!!!.......")
    else:
      dead("Well that could have went better!")



intro()
front_gate()





