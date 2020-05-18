print(13 > 8)
print(13 == 8)
print(13 < 8)
# booleans see if a statement is true or false

a = 14
b = 14.1
if a > b:
    print("a is greater than b")
else:
    print("a is less than b")
# you can use if/else to show two results

print(bool(178))
print(bool(False))
print(bool(["car", "boat", "plane"]))

class myclass():
  def __len__(self):
    return True

myobj = myclass()
print(bool(myobj))

x = 1.56
print(isinstance(x, int))
# checks if x is integer

x = 1.56
print(isinstance(x, float))
#checks if x is a float


