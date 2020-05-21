carlist = ["ford", "honda", "toyota", "BMW", "lexus", "nissan"]
print(carlist)

foodlist = ["chicken", "carrots", "yogurt", "pasta", "burger", "sandwich", "cheese"]
print(foodlist[3:6])

transportlist = ["car", "boat", "plane", "train", "rocket", "motorcycle"]
print(transportlist[:5])
print(transportlist[:2])

bodylist = ["arms", "legs", "head", "stomach", "nose", "feet"]
print(bodylist[-5:-2])

sportslist = ["basketball", "soccer", "tennis", "golf", "baseball", "cricket"]
sportslist[1] = "football"
print(sportslist)

carlist = ["ford", "honda", "toyota", "BMW", "lexus", "nissan"]
for x in carlist:
  print(x) 

foodlist = ["chicken", "carrots", "yogurt", "pasta", "burger", "sandwich", "cheese"]
if "pasta" in foodlist:
  print("Pasta is in this list")

transportlist = ["car", "boat", "plane", "train", "rocket", "motorcycle"]
print(len(transportlist))

bodylist = ["arms", "legs", "head", "stomach", "nose", "feet"]
bodylist.append("eyes")
print(bodylist)

planetlist1 = ["mercury", "venus", "earth", "mars"]
planetlist2 = ["jupiter", "saturn", "uranus", "neptune"]

solarsystem = planetlist1 + planetlist2
print(solarsystem) 

veggielist = list(("carrots", "corn", "lettuce"))
print(veggielist)


