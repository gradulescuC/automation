import time

import requests
from selenium import webdriver

# bbox = bounding box
# https://overpass-turbo.eu/#
# https://wiki.openstreetmap.org/wiki/Key:amenity

def osm_data(amenity, bbox):  # osm = openstreetmap
    url = "https://overpass.kumi.systems/api/interpreter" #continutul variabilei url este de fapt endpointul cu care vom trimite requestul
    query = '[out:json];node [amenity='+ amenity +'] ('+ bbox + '); out;'
    response = requests.get(url,params=
    { "data": query } # aici am dat ca si valoare pentru argumentul params un dictionar care contine corespondentul cheie("data"):valoare(query-ul definit anterior)
                            )
    return response.json()

print("------------------------")

a = osm_data("nightclub","53.2987342,-6.3870259,53.4105416,-6.1148829") #Am creat o varibila careia i-am atribuit ca si valore rezultatul apelarii functiei osm_data
b = osm_data("teatru","53.2987342,-6.3870259,53.4105416,-6.1148829") #La fel si aici

print(a)
print(b)

poa = a["elements"][0]["tags"]
adr = poa["addr:street"]
amn = poa["amenity"]
name = poa["name"]
ohr = poa["opening_hours"]
phn = poa["phone"]
web = poa["website"]
print(adr)
print(amn)
print(name)
print(ohr)
print(phn)
print(web)
driver = webdriver.Chrome("/Users/gradulescu/Desktop/Personal/Cursuri/ITF/Automation Course/Proiecte Python/RepositoryGithub/PythonAutomation/venv/04 - selenium_workshop_pom/resources/chromedriver")
driver.get(web)
time.sleep(2)
driver.quit()

# TODO check if key in dict, if true select and open the website, else do not do anything
