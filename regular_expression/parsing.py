import re


file_object  = open("erable.html", "r", encoding="utf8")

html = file_object.read()

pattern=re.compile("<title>(.+?)</title>")

title=re.findall(pattern, html)
print(title)
