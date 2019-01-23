import re

global_variable = "nada"

def find_html(html):
    #search first similarity and take all text from the first <b>
    extracted_html = re.findall(re.compile("<[Bb]>.*"), html)

    extracted_html = ''.join(extracted_html) # join the list to a string
    return extracted_html

def text_formating(extracted_html):
    #________________________REGEX_______________________
    # delete and replace every tags and formating.
    extracted_html = re.sub('<br>', ' ', extracted_html)
    extracted_html = re.sub('&eacute;', 'é', extracted_html)
    extracted_html = re.sub('&Eacute;', 'É', extracted_html)
    extracted_html = re.sub('&egrave;', 'è', extracted_html)
    extracted_html = re.sub('&ecirc;', 'ê', extracted_html)
    extracted_html = re.sub('&agrave;', 'à', extracted_html)
    extracted_html = re.sub('&acirc;', 'â', extracted_html)
    extracted_html = re.sub('&nbsp;', ' ', extracted_html)
    extracted_html = re.sub('<([Bb]|/[Bb]|[Aa]|/[Aa]|[Ii]|/[Ii])[^>]{0,}>', '', extracted_html)
    #____________________________________________________
    return extracted_html

def extract_title(html):
    # split when found the titles saving the (splited word)
    html = re.split('(Nom commun :|Nom latin :|famille :|catégorie :|port :|feuillage :|floraison :|couleur :|croissance :)', html)

    # extract the titles of the list that the split() return
    extracted_title = []
    for key, value in enumerate(html):
        if ((value == "Nom commun :") or (value == "Nom latin :") or
           (value == "famille :") or (value == "catégorie :") or
           (value == "port :") or (value == "feuillage :") or
           (value == "floraison :") or (value == "couleur :") or
           (value == "croissance :")):
            extracted_title.append(value)
    return extracted_title

def extract_content(extracted_html):
    extracted_html = ''.join(extracted_html)
    extracted_html = re.split('Nom commun :|Nom latin :|famille :|catégorie :|port :|feuillage :|floraison :|couleur :|croissance :', extracted_html)

    del(extracted_html[0]) # delete first entry because is always ''

    return extracted_html


def beautify_list():
    print("hey")
