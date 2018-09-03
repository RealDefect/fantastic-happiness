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

#need to working on fixing commented out items.
#also when running in GitBash text does not display asking for user input need to research defect

def front_gate():
	print "You wake up in a forest lush with green tree's." 
	print "In front of you a castle with a iron gate." 
	print "Do you find the lever to open the gate or walk the opposite direction?"
	castlegate = raw_input("> ")
        if castlegate == "open the gate":
            print "You stumble to the gate finding the lever."
            print "It opens slowly to a court yard. So many bushes around you can't count them all."
            print "You look around searching for anyone else."  
            court_yard()
            #else if castlegate == "walk the opposite direction":
              #print "You turn around and start walking into the forest."
               # print "You fall into a pit breaking your leg." 
	            #print "You scream for help but no one comes to your aide."
                #dead()
                #else:
                  #  print "You find a place to relax under a tree and fall asleep."
                   # front_gate()
		

# end game for the user 	
def dead():
	print "You died. Game Over!"
	exit(0)
	
def court_yard():
		print "You see a red, green, and blue door. Which door do you open?"
		door = raw_input("> ")
		
		if door == "red":
			red_door()
		elif door == "green":
			green_door()
		elif door == "blue":
			blue_door()
		else:
			print "You walk back to the forest and relax under a tree and fall asleep."
			front_gate()

def green_door():
	print  "As you get closer to the door it hums.... Strange...."
	print  "The door says please pick a number 1 through 10."
	print  "What number do you choose?"
	door_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	guessnumber = int(input())
	if guessnumber in door_list(0,4):
		print "You are allowed to enter."
		print "The door opens slowly for you."
		# need to write what happens next for the user 
	else:
		print "You are not allowed to enter." 
		print "Nothing else happens......."
		court_yard()

def red_door():
	print "The door is locked. You need a key to unlock it."
	court_yard()
	
def blue_door():
	print "The door opens slowly, to room filled with gold coins."
	print "How many coins do you take ?" 
	pockets = int(input())
	if pockets <= 500:
		print "You place a handful of coins in your pocket." 
		print "You quickly shut the door before anyone sees you. "
		print "You run outside the gate it slams closed behind you."
		front_gate()
	else:
           #print "As you are filling your pockets with gold something moves."
		   #print "Suddenly a snack leaps out from under the coins bitting you."
           #print "Everything goes dark!!!......."
		   dead()


	
front_gate()





