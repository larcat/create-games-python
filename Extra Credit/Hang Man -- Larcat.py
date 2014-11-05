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

def word_show(word):
    base = "_" * (len(random_word) - 1)
    result = ''
    for ch in base:
       result = result + ch + ' '
    print(result[:-1])

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

word_show(random_word)    
gallows_1()






