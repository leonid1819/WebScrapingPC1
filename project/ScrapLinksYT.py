import requests
import gspread

from bs4 import BeautifulSoup
import re
import json

gc = gspread.service_account(filename='webscrapingurls-8c796a18ea3a.json')
sh = gc.open("VideosYoutube")
worksheet = sh.get_worksheet(0)


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

ente=3
carac='D'
for data in content:
    for key, value in data.items():
        if type(value) is dict:
            
            for k,v in value.items():
                
                if k=="videoId" and len(v) == 11:
                    worksheet.update(carac+f'{ente}',v)
                    ente=ente+1
                    print(ente)
                    print(v)
                