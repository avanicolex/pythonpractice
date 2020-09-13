#This is a comment
#print writes to console
print('kajfkldj')

## name the variable, set it with =
myName = "ava"
up = 2
low = 2.4
isTrue = True
## if condition
## = means "set this to"
## == means "if these two are equal" or "is equal to"
## one tab to do what you want to do if the condition evaluates true
if myName == "ava":
    print('My name is Ava')

print('isTrue =', isTrue)

if low < up:
    isTrue = False

print('isTrue =', isTrue)


#def means define 
# its a way to store a block of code inside of a "function", which is like a variable for code
def compare(n1 = "x", n2 = "x"):
    try:
        ## cant do this, because you cant assign a function return to a function call
        #float(n1) = input("enter a number: ")
        #float(n2) = input("enter a number: ")
        if n1 == "x" and n2 == "x":
            n1 = float(input("enter a number: "))
            n2 = float(input("enter a number: "))
        elif n1 == "x":
            n1 = float(input("enter a number: "))
        elif n2 == "x":
            n2 = float(input("enter a number: "))

        print('n1 =', type(n1))
        print('n2 =', type(n2))

        if n1 < n2:
            print("less")
        elif n1 > n2:
            print("more")
        else:
            print("idk bruh")
    except:
        print("that's not a number retard")




n3 = 5
n4 = 10
compare()
compare(n3)
compare(n3, n4)


#int(n1)
#int(n2)

## a string (str) is anything in quotes "this is a string"
## an int is a whole signed number, 1, -2
## a float is a floating point number

#all input is a string, so this doesnt work for eval
##if type(n1) is str or type(n2) is str:
    ##print("that's not a number yo")




