print("Try to correctly predict if the coin will land on HEADS or TAILS")
print("Pick 1 for HEADS and Pick 2 for TAILS")
userGuess = input("Pick HEADS or TAILS (1 or 2): ")
prediction = int(userGuess)

print(" ")
print("Flipping coin...")
print(" ")
import time
time.sleep(1.25)

import random
coinResult = random.randint(1,2)

if coinResult == 1:
    print("The coin landed on HEADS")
elif coinResult == 2:
    print("The coin landed on TAILS")

if coinResult == prediction:
    print("You predicted the flip correctly")
else:
    print("You predicted the flip incorrectly")

