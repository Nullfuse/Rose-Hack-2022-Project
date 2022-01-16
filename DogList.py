#--------------------------BACKEND--------------------------
#Stores Dog Name, Age, Gender, Breed
#infoList will be a list of strings corresponding to
#a Dog's Name, Age, Gender, and Breed
class Dog:
  def __init__(self, infoList):
    self.name = infoList[0]
    self.age = infoList[1]
    self.gender = infoList[2]
    self.breed = infoList[3]

  def to_string(self):
    return self.name + "|" + self.age + "|" + self.gender + "|" + self.breed

def readList(doglist, DOG_INFO_TYPES):
  # Open file containing all saved dog information
  with open('doglist.txt') as f:
    lines = f.readlines()
    print(lines)
  f.close()

  # Insert saved dogs into list
  lineCount = 0
  for line in lines:
    ++lineCount
    line = line.split('|')
    # Check for DOG_INFO_TYPES number of delimited arguments
    if len(line) != DOG_INFO_TYPES + 1:
      print("Incorrect number of arguments on line " + str(lineCount))
    # Add new Dog to doglist with specified information
    else:
      newDog = Dog(line)
      doglist.append(newDog)

# Saving items in the list to file
def saveList(doglist):
  if len(doglist) > 0:
    with open('doglist.txt', 'w') as f:
      for dog in doglist:
        f.write(dog.to_string() + "|\n")
    f.close()
#-----------------------------------------------------------