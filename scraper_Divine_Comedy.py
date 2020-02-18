"""
This script downloads Dante Alighieri's Divina Commedia and stores it in the
current folder in .txt format.
It takes sources from two separate Wikisource pages, one for Canti's titles
and descriptions, one for the respective bodies of text. This decision complicated
the script but improved formatting.

Final .txt required few manual corrections:
Removing spaces around aphostrophes (') at:
    - Inferno: (II, 89), (III, 19) (VIII, 120), (XVI, 124), (XX, 37)
    - Purgatorio: (VIII, 3)
    - Paradiso: (XXVII, 19)

"""

import os
import re
import requests
from bs4 import BeautifulSoup
from roman import toRoman


def get_titles(part):
    """
    THis function extracts the titles and the descriptions of the Canti's of
    each part (Inferno, Purgatorio, Paradiso). It returns them as a list of str
    """

    ## GET html data
    page = requests.get('https://it.wikisource.org/wiki/Divina_Commedia/' + part)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Take text data
    text = soup.find_all('i')

    ## Extract the Canti name/numbers and their subtitles
    text = [ element.get_text() for element in text ]
    text = [ element.strip() for element in text ]
    text = [ element.replace("’", "'") for element in text ]

    canti_titles_list = []

    ## Pair them
    for i in list(range(0, len(text), 2)):
        canti_titles_list.append(text[i] + '\n' + "[" +text[i+1] + "]")

    return canti_titles_list



def scrape_canto(url):
    """
    Scrapes the body of each Canto. Source: Wikisource
    """
    ## Get html data
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    ## Get Canto
    body = soup.find_all('div', class_='poem')
    body = [ verse.get_text() for verse in body ]

    body = "\n".join(body)
    body = body.replace("\xa0", u" ")
    body = body.replace("«", u"\"")
    body = body.replace("»", u"\"")
    body = body.replace("’", u"'")
    body = body.replace(" .mw-parser-output .numeroriga{float:right;color:#666;font-size:70%}3", u"")
    body = body.strip()

    return body



def scrape_part(part):
    """
    Iterates Canti's scraper on the whole part, combines them with Canti's
    titles list, then assembles it in a single str.
    """
    part_titles = get_titles(part)

    whole_part = []
    base_url = "https://it.wikisource.org/wiki/Divina_Commedia/{}/Canto_".format(part)

    for i in range(len(part_titles)):
        canto = scrape_canto(base_url + toRoman(i+1))
        canto = part_titles[i] + '\n\n' + canto
        whole_part.append(canto)

    whole_part = "\n\n\n".join(whole_part)
    whole_part = part.upper() + "\n\n\n" + whole_part + "\n\n\n\n\n"

    return whole_part



def assemble_the_Comedy():

    Inferno =  scrape_part("Inferno")
    Purgatorio =  scrape_part("Purgatorio")
    Paradiso =  scrape_part("Paradiso")

    DivinaCommedia = Inferno + Purgatorio + Paradiso

    return DivinaCommedia




if __name__ == "__main__":

    import time
    start = time.time()

    DivinaCommedia = assemble_the_Comedy()

    # Writes .txt in current directory
    txt_file = open(r"DivinaCommedia.txt", "w+")
    txt_file.write(DivinaCommedia)
    txt_file.close()

    stop = time.time()
    print('\nFile generated in ' + str(round(stop-start, 3)) + ' seconds.')
