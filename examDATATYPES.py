# Problem 1
#=================================

# Price of a year book
price = "25.0"

# Number of year books sold
numSold = 812

# print data type of the price variable

print(type(price))

# print data type of the numSold variable

print(type(numSold))

# print the sale amount (price * numSold)

numPrice = float(price)
totalPrice = ( numPrice * numSold)
print(totalPrice)


# Problem 2
#=====================================================

text = "We live in Knoxville, tn"
# Print the length of the text string

print(len(text))

# Convert "tn" to upercase and then print the text

print(text.replace("tn", "TN"))

# Print the location of the letter "K" in the text

print(text.index("K"))

# Replace the word "We" with "They" and then print the text

print(text.replace("We", "They"))

# Problem 3
#======================================================

weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Print the number of items in weekDays list

print(len(weekDays))

# Print the third item in the weekDays list

print(weekDays[2])

# Print the last four items in the weekDays list

print(weekDays[3:7])

# Change the first item to "MONDAY" and then print the list

weekDays[0] = "MONDAY"
print(weekDays)

# Print the list in reverse order

weekDays.reverse()
print(weekDays)