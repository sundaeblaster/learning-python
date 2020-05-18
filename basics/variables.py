f = "strawberry"

def fruitchoice():
    global f
    f = "mango"
    print("I would like to eat a " + f )

fruitchoice()

print("I would like to eat " + f)
# variables are only known inside a function
# "global" overwrites a variable