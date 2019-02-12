import re  # module re

# open file
file_object  = open("string.txt", "r", encoding="utf8")
string = file_object.read()

# With space at start :
print(string)

string = re.sub('^\s', '', string)

# Without space at start :
print(string)
