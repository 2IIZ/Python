import re  # module re

file_object  = open("erable.html", "r", encoding="utf8")

html = file_object.read()

#___________________________________________________________________
title_pattern = re.compile("<TITLE>(.+?)</TITLE>")
# find the pattern then print what's found.
title = re.findall(title_pattern, html) # findall() takes all results
print(title, "\n")
#___________________________________________________________________
