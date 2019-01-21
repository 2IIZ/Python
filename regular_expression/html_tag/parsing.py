import re  # module re


file_object  = open("erable.html", "r", encoding="utf8")

html = file_object.read()

title_pattern = re.compile("<TITLE>(.+?)</TITLE>")
# find the pattern then print what's found.
title = re.findall(title_pattern, html) # findall() takes all results
print(title, "\n")

# search() will take the first result
p_pattern = re.compile("<[Bb]>.*")

extracted_html = re.findall(p_pattern, html)
extracted_html = ''.join(extracted_html)
# extracted_html = re.sub('<([Bb])>', '', extracted_html)
# extracted_html = re.sub('</([Bb])>', '', extracted_html)
extracted_html = re.sub('<br>', '', extracted_html)
extracted_html = re.sub('&eacute;', 'é', extracted_html)
extracted_html = re.sub('&Eacute;', 'É', extracted_html)
extracted_html = re.sub('&egrave;', 'è', extracted_html)
extracted_html = re.sub('&ecirc;', 'ê', extracted_html)
extracted_html = re.sub('&agrave;', 'à', extracted_html)
extracted_html = re.sub('&acirc;', 'â', extracted_html)
extracted_html = re.sub('&nbsp;', ' ', extracted_html)
# extracted_html = re.sub('<a [^>]{0,}>', '', extracted_html)
extracted_html = re.sub('<([Bb]|/[Bb]|[Aa]|/[Aa]|[Ii]|/[Ii])[^>]{0,}>', '', extracted_html)

# extracted_html = extracted_html.split('Nom commun : ')
# extracted_html = extracted_html.split('Nom latin : ')

# splited in two but list so cannot use it another time.
# so the good thing to do is to save it when splited




print(extracted_html)
