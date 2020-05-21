x = "I like to use Python"
print(x[4])

y = "Hi Tom"
print(len(y))

a = "    Give me some apples!  "
print(a.strip())

b = "Today is Friday"
print(b[3:7])
# can be used with negative numbers to display characters backward

c = "HAPPY BIRTHDAY"
print(c.lower())
# replace lower with upper to captalize all the letters

money = "I have 20 dollars in my bank account"
m = "20" in money
print(m)

money2 = "I have 20 dollars in my bank account"
m2 = "30" in money
print(m2)
# lines 18-24 use "in" which can veerify if a certain part of the string is there

time = 7
flight = "The flight will be {} hours long"
print(flight.format(time))

gate = "E5"
time = "5:30"
destination = "Miami"
txt = "We need to go to gate {} at {} to board our flight to {}"
print(txt.format(gate, time, destination))
# can put numbers in the curly brackets to show which variable goes where (start with 0)

q = "The popular band \"Twenty One Pilots\" is coming to town"
print(q)
# use backslashes to type illegal characters
