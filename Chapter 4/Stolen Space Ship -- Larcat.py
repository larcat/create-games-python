# Import random number generator
import random

# Intro the game/give instructions

print()
print("Welcome to Space Ship Thief!")
print()
print("You have stolen a Space Yacht to escape from planet Yuxnor.")
print("The owner, a Yuxnorian army officer, wants his ship back.")
print("Some of his Yuxnorian thug buddies are chasing you in their ships.")
print("Survive the perils of the void, and make it to planet Awesome safely.")
print()

done = False
user_command = " "
parsecs_travelled = 0
total_travelled = 0
computer_mood = 0
fuel_loaded = 5
unobtanium = 15
parsecs_back = -20

# Main game loop
while done == False:
    
    # Status checks with Ifs. Possible deaths.
    if unobtanium + fuel_loaded < 5:
        print()
        print("You are low on unobtanium! You only have ", unobtanium + fuel_loaded, " between the reactor and your stores!")

    if computer_mood > 10:
        print()
        print("Jimmy, the artificially intelligent Computer Co-Pilot finally snaps, wresting control of the vessel from you!")
        print("Jimmy sends you shooting into an asteroid field... You are never heard from again.")
        print("Game over.")
        done = True
    
    if unobtanium + fuel_loaded < 1:
        print()
        print("You are out of fuel, adrift in the void!")
        print("The Yuxnorians catch you, ripping into the hull of the Yacht...")
        print("You are never heard from again.")
        print("Game over.")
        done = True
    
    if parsecs_back >= 0:
        print("The Yuxnorians catch you, ripping into the hull of the Yacht...")
        print("You are never heard from again.")
        print("Game over.")
        done = True
        
    if parsecs_back >= 10:
        print("Jimmy, the artificially intelligent computer co-pilot, says 'Sensors detect the Yuxnorians closing in!")
    
    if total_travelled >= 100:
        print("Famished, beaten and bruised, you arrive at Planet Awesome!")
        print("You are heralded as a hero for thumbing your nose at the hated Yuxnorians!")
        print("Well done! You win!")
        done = True
        
    # User commands
    print()
    print("A. Add unobtanium to the hyper drive.")
    print("B. Hyperdrive engage. 50% speed of light")
    print("C. Hyperdrive engage. 98% speed of light")
    print("D. Cool hyperdrive impellers for 1 solar cycle.")
    print("E. 'Computer, systems check!'")
    print("Q. Quit.")
    print()
    user_command = input("Issue your commands, space pirate: ")
    
    # Quit statement
    if str.lower(user_command) == "q" or str.lower(user_command) == "quit":
        print("Quitters never win.")
        print("Exiting.")
        done = True
    
    # Status update with variable computer moods    
    elif str.lower(user_command) == "e":
        print()
        if computer_mood <=4:
            print("The artificially intelligent Co-Pilot Computer, Jimmy, is composed.")
        elif computer_mood <= 7:
            print("The artificially intelligent Co-Pilot Computer, Jimmy, is cranky.")
        elif computer_mood <= 7:
            print("The artificially intelligent Co-Pilot Computer, Jimmy, is FURIOUS*@#($&@.")
        print("Unobtanium loaded in Hyperdrive = ", fuel_loaded)
        print("Extra unobtanium stores = ", unobtanium)
        print("The Yuxnorian thugs are, ", parsecs_back, "parsecs behind you in space")
    
    # Solar cycle rest
    elif str.lower(user_command) == "d":
        computer_mood = 0
        parsecs_back = parsecs_back + random.randrange(6, 14)
        print()
        print("The artificially intelligent Co-Pilot Computer, Jimmy, seems less on edge.")
        print("You suspect the the Yuxnorian thugs have caught a few parsecs.")
    
    # Ahead full speed
    elif str.lower(user_command) == "c":
        parsecs_travelled = random.randrange(10, 21)
        total_travelled = total_travelled + parsecs_travelled
        parsecs_back = parsecs_back + random.randrange(6, 14) - parsecs_travelled
        computer_mood = computer_mood + random.randrange(1, 4)
        fuel_loaded = fuel_loaded - random.randrange(1, 4)
        print()
        print("You zoom forward, ", parsecs_travelled, " parsecs in space.")
        if computer_mood <=4:
            print("The artificially intelligent Co-Pilot Computer, Jimmy, is composed.")
        elif computer_mood <= 7:
            print("The artificially intelligent Co-Pilot Computer, Jimmy, is cranky.")
        else:
            print("The artificially intelligent Co-Pilot Computer, Jimmy, is FURIOUS*@#($&@.")
            
    # Ahead moderate speed
    elif str.lower(user_command) == "b":
        parsecs_travelled = random.randrange(5, 13)
        total_travelled = total_travelled + parsecs_travelled
        parsecs_back = parsecs_back + random.randrange(6, 14) - parsecs_travelled
        computer_mood = computer_mood + random.randrange(1, 2)
        fuel_loaded = fuel_loaded - random.randrange(1, 2)
        print()
        print("You zoom forward, ", parsecs_travelled, " parsecs in space.")
        if computer_mood <=4:
            print("The artificially intelligent Co-Pilot Computer, Jimmy, is composed.")
        elif computer_mood <= 7:
            print("The artificially intelligent Co-Pilot Computer, Jimmy, is cranky.")
        else:
            print("The artificially intelligent Co-Pilot Computer, Jimmy, is FURIOUS*@#($&@.")

    # Refuel
    elif str.lower(user_command) == "a":
        if unobtanium >= 5:
            computer_mood = computer_mood -4
            unobtanium = unobtanium - 5
            fuel_loaded = fuel_loaded + 5
            print()
            print("While zooming through the void, you load 5 ingots of precious unobtanium into the hyperdrive.")
            print("Jimmy, the artificially intelligent Co-Pilot Computer says 'Thank you for the food.'")
            print("The artificially intelligent Co-Pilot Computer, Jimmy, seems less on edge.")
            
        elif unobtanium > 0:
            computer_mood = computer_mood - 1
            fuel_loaded = fuel_loaded + unobtanium
            print()
            print("While zooming through the void, you load, ", unobtanium, " ingots of precious unobtanium into the hyperdrive.")
            print("Jimmy, the artificially intelligent Co-Pilot Computer says 'Thank you for the food.'")
            print("The artificially intelligent Co-Pilot Computer, Jimmy, seems less on edge.")              
            unobtanium = 0
            
        elif unobtanium == 0:
            computer_mood = computer_mood + 3 
            print()
            print("You have no more unobtanium in storage. You have ", fuel_loaded, "in the reactor.")
            print("Jimmy, the artificially intelligent Co-Pilot Computer says 'I am not pleased. Where is the food?'")
            print("The artificially intelligent Co-Pilot Computer, Jimmy, agitated.")              

            
        
        
    
              
    
        
    
        
    
    
    