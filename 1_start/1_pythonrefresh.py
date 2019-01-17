# @Date:   2019-01-01T11:10:47+01:00
# @Last modified time: 2019-01-03T10:36:42+01:00

# f5 to run
# Python Refresh for using Django

print(" _______________________VARIABLES______________________\n\n")


type(3) #-> <class 'int'>
type("fwa") #-> <class 'str'>
type(3.4) #-> <class 'float'>


# the variable age is now an Int of 20
age = 20
# the variable name is "Ivan"
name = "Ivan"
# print my name and my age using format()
print("Hello my name is {} and my age is {}\n\n".format(name, age))


print(" _______________________CONDITION______________________\n\n")

# set variable boolean -> True or False
boolean = False

# if my age is strictly greater than 18, print() and change boolean to True
# you can use all these operators : '<' '>' '<=' '>=' '==' '!='
if age > 18:
    print("You're older than 18")
    boolean = True
#if I'm under 18, print() but don't change the boolean
else:
    print("You're too young !")

# if boolean is True then print()
if boolean:
    print("The boolean is True")

print("\n")


print(" _______________________FUNCTION______________________\n\n")

def hello(theString):
    print("Starting with " + theString)

hello("a string made by hand")


print("\n")


print(" ________________________LISTS_______________________\n\n")

dogNames = ["Jax", "Cro", "Iv", "Squalo"]

#print list
print("List of dogs :", dogNames)

#add one item
dogNames.insert(0, "AddedTo0")
print("One dog added :", dogNames)

#show one item
print("Showing the [3] one :", dogNames[3])

#del one item
del(dogNames[4])
print("The dog [4] is lost =(", dogNames)

# add an item to the end of the list
dogNames.append('NewOne')
print("We found a new one :", dogNames[-1]) # [-1] -> shows the last item

#length of list
print("There is", len(dogNames), "dogs")
print("List of dogs :", dogNames)


print("\n")

print(" _______________________LOOPS______________________\n\n")

for dog in dogNames:
	print(dog)

print("\n")

#go through 0 to 10
for x in range(0, 6):
	print(x)

print("\n")

bool = True
#verify if it's true then print true
while bool == True:
	print(bool)
	bool = False


print(" _______________________DICTIONARIES______________________\n\n")

goats = {"Fido":8, "Camop":10, "Thor":4}

#print the age of Fido !
print(goats["Fido"])

#kill one goat
del(goats["Camop"])

#new born
goats["Pedro"] = 0

#print all goats
print(goats)

print("\n")

print(" _______________________CLASS______________________\n\n")

class Goat:
	goatInfo = "Goat are masters"

	#self is added to show the inner content (python's practice)
	def __init__(self, name, age, furcolor):
		self.name = name
		self.age = age
		self.furcolor = furcolor

	# bleat = bark for a goat
	def bleat(self):
		print("BEEEEEE")

mygoat = Goat("Jax", "2", "Red")
mygoat.bleat()


print(mygoat.name)
print(Goat.goatInfo)
