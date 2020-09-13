####################################################################
#  TO DO LIST: 
# - check for Y and N in the input from readInput, AND figure out how to deal with upper/lower case and whitespace in strings
# -    try to do this without using any more if statements (so not just... if Y or if N or if y or if n)
# - ask the user if they are okay with their list, and let them optionally remove specific items from it
# - ask user if they want to add to numlist, get their input, then add all the numbers in the list and print it
# - figure out how to use strings that are stored in one of your lists and combine them into one string, with commas in between
#      for example:  ["you", "me"]  becomes "you, me"
####################################################################


#Always document your code! T\

# Name: listsAndLoops.py
# Author: https://github.com/avanicolex

# Purpose of this Program: 
# ask the user if they want to add to the fruit list
# if yes, ask how many times and let them add a fruit to the list for that amount of times
# ask the user if they want to add to the color list
# if yes, ask how many times and let them add a color to the list for that amount of times
# ...
# ... (As you get through the to-do-list, update this)
# ...


# Variables in the GLOBAL Scope (these are available to use for all functions)

colorList = ["pink", "blue"]
fruitList = []
numList = [0, 4, 2]

# Functions in the GLOBAL Scope (these are available for the whole program to use) 

def main():
    i = input("would you like to add to the fruit list?: y/n  ")
    a = readInput(i, "how many would you like to add?: ")
    addToListANumberOfTimes(a, "enter fruit: ", fruitList)

    i = input("would you like to add to the color list?: y/n  ")
    a = readInput(i, "how many would you like to add?: ")
    addToListANumberOfTimes(a, "enter color: ", colorList)

    print("The fruitlist contains: ", fruitList)
    print("The colorlist contains: ", colorList)
    print(fruitList[0])


def readInput(i, nextQuestion):
    if i == "y":
        return input(nextQuestion)

## Purpose: lets the user give input a number of times to add to a list
## Arguments:
#### number -> the number of times to add to the list
#### msg -> what should we ask the user for
#### theList -> which list to add the input to

def addToListANumberOfTimes(number, msg, theList):
    try:
        number = int(number)
        for x in range(number):
            theList.append(input(msg))
    except:
        print("something went wrong")



## we run main because it is our main program
## the functions we define above are the logic for the program, that main uses to determine what to do
## This is where you call main (the function you defined above), which runs your program!

main()