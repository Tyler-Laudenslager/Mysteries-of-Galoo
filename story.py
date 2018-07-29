#Kandu! Entertainment est. 6/30/2018
#This is the story module for Mysteries of Galoo.

from time import sleep

def welcome_to_galoo():
    clear_buffer()
    print("""

Welcome to Mysteries of Galoo!
_________________________________________________________________

Far away near the dark mountain of Soochun lives a formitable foe,
Kathun the Enforcer. Wise young traveler you are all we have hoped
for in these last few days. Trek wisely through Galoo and defeat Kathun
before dark powers annihilate the land. """)

    blank_lines(4)
    ## I would suggest to replace this sleep(2) with a "press /whatever/ to continue" 
    ## to allow the player to read the story. -Austin
    sleep(2)

# blank_lines inserts n blank lines when called.
## Typical usage: Visual alignment of elements
def blank_lines(n):
    for i in range(n):
        print()

# clear_buffer fills terminal with empty lines. 128 being a number 
## I chose with intent to cover the vertical size of different terminals
## This can be adjusted as needed.
def clear_buffer():
    blank_lines(128)
    
