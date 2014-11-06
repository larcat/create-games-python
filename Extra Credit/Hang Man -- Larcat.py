# TODO -- Clean up utility calls/prints. finish testing # of chances. Finish commenting.

#import random number generator
import random


# Word list
source_file = "wordlist.txt"
# Global storage for random word
random_word = " "

incorrect = 0

# Picks a random word from the wordlist
def random_pick(file):
    
    # Defining used variables
    random_line = " "
    
    # Does the picking
    random_line = random.choice(open(file).readlines())
    
    # Make sure word list is closed
    f = open(file)
    f.close()
    
    # This checked to see if the file was closed
    
    #if f.closed:
      #print("file is closed")
      
    return random_line

random_word = random_pick(source_file) 

print(random_word)

random_word_length = len(random_word)

#gallows_1 == no body parts
#gallows_2 == 1 body part
#gallows_3 == 2 body parts..... etc
#gallows_8 == dead

def gallows_1():
    print()
    print("     ----     ")
    print("    /    \    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("    --------- ")
    
def gallows_2():
    print()
    print("     ----     ")
    print("    /    \    ")
    print("   O     |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("    --------- ")

def gallows_3():
    print()
    print("     ----     ")
    print("    /    \    ")
    print("   O     |    ")
    print("   |     |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("    --------- ")

def gallows_4():
    print()
    print("     ----     ")
    print("    /    \    ")
    print("   O     |    ")
    print("  \|     |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("    --------- ")

def gallows_5():
    print()
    print("     ----     ")
    print("    /    \    ")
    print("   O     |    ")
    print("  \|/    |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("    --------- ")

def gallows_6():
    print()
    print("     ----     ")
    print("    /    \    ")
    print("   O     |    ")
    print("  \|/    |    ")
    print("   |     |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("    --------- ")
   

def gallows_7():
    print()
    print("     ----     ")
    print("    /    \    ")
    print("   O     |    ")
    print("  \|/    |    ")
    print("   |     |    ")
    print("  /      |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("    --------- ")

def gallows_8():
    print()
    print("     ----     ")
    print("    /    \    ")
    print("   O     |    ")
    print("  \|/    |    ")
    print("   |     |    ")
    print("  / \    |    ")
    print("         |    ")
    print("         |    ")
    print("         |    ")
    print("    --------- ")
    
gallows_list = [gallows_1, gallows_2, gallows_3, gallows_4, gallows_5, gallows_6, gallows_7, gallows_8]

# MAIN LOOP
# Pick a letter code
# MAIN LOOP
def guess_reconcile(random_word):
    
    # Defining variable
    current_guess = None
    death_count = 0
    
    # Turning random_word into a string
    random_word = random_word.replace('\n', '')
    
    # Creating empty string of length of random_word
    current_solved = ['_'] * len(random_word)
    
    def guess_check(current_guess, current_solved):
        print()
        
        # Main loop check variable
        
        death_count = 0
        
        while death_count < len(random_word):
            
            print ()
            print("The fate of this poor bastard rests in your guessing hands...")
            print()
            
            gallows_list[death_count]()
        
            current_guess = input("Please enter your guess: ")
    
            while len(current_guess) > 1 or str.isalpha(current_guess) == False:
                print()
                print("Your guess must be only a single letter, no numbers!")
                current_guess = input("Please enter your guess: ")
        
            if str.lower(current_guess) in random_word:
                print()
                print("You saved the falsely accused from a step in the hanging!", current_guess, "is in the word!")
                for i, ch in enumerate(random_word):
                    if current_guess == random_word[i]:
                        current_solved[i] = current_guess
                
                if "_" not in current_solved:
                    print()
                    print("You saved that poor bastard!")
                    print()
                    print("The random word was:", random_word)
                    break
            
            else:
                print()
                print("You want this poor bastard to die.", current_guess, "is NOT in the random word!")
                death_count += 1
                
                if death_count >= 8:
                    print()
                    print("That poor bastard died! Look what you did!")
                    break
                
            # Cleans up current_solved printing
            print(" ".join(str(x) for x in current_solved))
    
    guess_check(current_guess, current_solved)

guess_reconcile(random_word)








