import re

flor_titles = "Nom commun :|Nom latin :|famille :|catégorie :|port :|feuillage :|floraison :|couleur :|croissance :|fruits :|hauteur :|plantation :|multiplication :|sol :|emplacement:|zone :|origine :|entretien :"



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
    html = re.split('('+ flor_titles +')', html)

    # extract the titles of the list that the split() return
    extracted_title = []
    raw_titles = flor_titles.split("|")

    # loop through the html splited
    for html_title_key, html_title_value in enumerate(html):
        # loop into the titles of raw title to verify if it's equals to html splited
        # and store them in a list
        for raw_title_key, raw_title_value in enumerate(raw_titles):
            if (html_title_value == raw_title_value):
                extracted_title.append(html_title_value)
    return extracted_title



def extract_content(extracted_html):
    extracted_html = ''.join(extracted_html)
    extracted_html = re.split(flor_titles, extracted_html)

    del(extracted_html[0]) # delete first entry because is always ''

    return extracted_html


def beautify_list():
    print("hey")
