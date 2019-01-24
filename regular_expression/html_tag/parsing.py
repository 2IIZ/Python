import re  # module re
from modules.mylibrary import *  #____My library____

# open file
file_object  = open("erable.html", "r", encoding="utf8")
html = file_object.read()

# search and find html from the page, return string html
extracted_html = find_html(html)

# delete tags and replace formating, return string
extracted_html = text_formating(extracted_html)

# extract title (->"Nom commun :"<- "content") from the split, return list
extracted_titles  = extract_title(extracted_html)

# extract content ("Nom commun :" ->"content"<-) from the split, return list
extracted_content = extract_content(extracted_html)


list={}
# link the two list together
for x in range(0, len(extracted_titles)):
    list[extracted_titles[x]] = extracted_content[x]
# print it
for key, value in list.items():
	print(key, value, "\n")
