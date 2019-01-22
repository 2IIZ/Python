import re  # module re

#____My library____
from modules.mylibrary import *

file_object  = open("erable.html", "r", encoding="utf8")
html = file_object.read()

#search first similarity and take all text from teh first <b>
p_pattern = re.compile("<[Bb]>.*")
extracted_html = re.findall(p_pattern, html)

extracted_html = ''.join(extracted_html) # join the list to a string

# delete tags and replace formating
extracted_html = text_formating(extracted_html)

# extract title ("Nom commun :" ...) from the split
titles  = extract_title(extracted_html)

extracted_html = ''.join(extracted_html)
extracted_html = re.split('Nom commun :|Nom latin :|famille :|catégorie :|port :|feuillage :|floraison :|couleur :|croissance :', extracted_html)

del(extracted_html[0])

# print(titles)
# print(extracted_html)

list={}

for x in range(0, len(titles)):
    list[titles[x]] = extracted_html[x]

for key, value in list.items():
	print(key, value, "\n")


print(global_variable) # replace the "Nom commun :" with variables
