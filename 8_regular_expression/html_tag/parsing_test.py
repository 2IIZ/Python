import re  # module re (Regular expression)

file_object  = open("erable.html", "r", encoding="utf8") # open file (html from wikipedia)

html = file_object.read() # read the file and save it to a variable

#___________________________________________________________________
# will save the regular expression in a variable
title_pattern = re.compile("<TITLE>(.+?)</TITLE>") # this specific regex find the title of the wikipedia page

# find the pattern then print what's found.
title = re.findall(title_pattern, html) # findall() takes all results
print(title, "\n") # print 
#___________________________________________________________________
