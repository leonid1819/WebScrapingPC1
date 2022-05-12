"""import requests
from bs4 import BeautifulSoup
import re
import json

url="https://www.youtube.com/results?search_query=python"

response=requests.get(url).text
soup = BeautifulSoup(response, 'lxml')
#
with open ("script.txt","w",encoding="utf-8") as output:
    output.write(soup.prettify())
#
script = soup.find_all("script")[39]

json_text = re.search('var ytInitialData = (.+)[,;]{1}',str(script)).group(1)
#
with open ("script.txt","w",encoding="utf-8") as output:
    output.write(json_text)
#

json_data = json.loads(json_text)

content = (
    json_data
    ['contents']['twoColumnSearchResultsRender']
    ['primaryContents']['sectionListRenderer']
    ['contents'][0]['itemSectionRender']
    ['contents']
)

for data in content:
    for key, value in data.items():
        if type(value) is dict:
            for k,v in value.items():
                if k=="videoId" and len(v) == 11:
                    print(v)
                if k == "thumbnail" and "thumnails" in v:
                    print(v["thumbnails"][0]["url"]+'\n')
"""