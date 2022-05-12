import requests
from bs4 import BeautifulSoup
import re
import json

url="https://www.youtube.com/results?search_query=python"

response=requests.get(url).text
soup = BeautifulSoup(response, 'lxml')

script = soup.find_all("script")[34]
json_text = re.search('var ytInitialData = (.+)[,;]{1}',str(script)).group(1)

json_data = json.loads(json_text)

content = (
    json_data
    ['contents']['twoColumnSearchResultsRenderer']
    ['primaryContents']['sectionListRenderer']
    ['contents'][0]['itemSectionRenderer']
    ['contents']
)
for data in content:
    for key, value in data.items():
        if type(value) is dict:
            for k,v in value.items():
                if k=="videoId" and len(v) == 11:
                    print(v)
                