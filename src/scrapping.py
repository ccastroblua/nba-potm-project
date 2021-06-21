import pandas as pd
import seaborn as sns

import requests
from bs4 import BeautifulSoup

import json


# Let's make a function to clean each row of information get from the html file:

def clear_row(pom):
    
    dic_poms = dict()

    dic_poms["season"] = pom[0].text
    dic_poms["player"] = pom[1].text
    dic_poms["conference"] = pom[2].text
    dic_poms["pom_month"] = pom[3].text
    dic_poms["team"] = pom[4].text.strip()
    dic_poms["position"] = pom[5].text
    
    return dic_poms


# We insert the soup content into this function to get the final "player of the month" dataset:

def html_cleaning(soup):
    poms_table = soup.find("tbody")
    pom_list = poms_table.find_all("tr")
    
    pom_db = [clear_row(pom.find_all("td")) for pom in pom_list]
    
    return pom_db 


# Now we proceed with the web scrapping and use of the defined functions:

url_nba = "https://basketball.realgm.com/nba/awards/by-type/Player-Of-The-Month/29"

response = requests.get(url=url_nba)

response.status_code

new_soup = BeautifulSoup(response.content, features="html.parser")


# Using html_cleaning function:

pom_dataset = html_cleaning(new_soup)


# Finally, we export the a JSON file with "player of the month" database.

jsonString = json.dumps(pom_dataset)

jsonFile = open("../data/pom_database.json", "w")

jsonFile.write(jsonString)

jsonFile.close()