from xml.etree.ElementTree import canonicalize
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs # importar bs
from googleapiclient.discovery import build
import gspread
import json
import re

url="https://www.youtube.com/watch?v=fPdqGQqYt70"


session = HTMLSession()

response = session.get(url)

response.html.render(sleep=1,timeout=60)

soup = bs(response.html.html, "html.parser")
data = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)

data_json = json.loads(data)
videoPrimaryInfoRenderer = data_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']
videoSecondaryInfoRenderer = data_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][1]['videoSecondaryInfoRenderer']

likes_label_aux = videoPrimaryInfoRenderer['videoActions']['menuRenderer']['topLevelButtons'][0]['toggleButtonRenderer']['accessibilityData']['accessibilityData']['label']
if likes_label_aux == "Me gusta":
    likes_label = "oculto"
else:
    likes_label = videoPrimaryInfoRenderer['videoActions']['menuRenderer']['topLevelButtons'][0]['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label'] # "No likes" or "###,###"
likes_str = likes_label.split(' ')[0].replace(',','')
print(likes_str)

   # likes_label = videoPrimaryInfoRenderer['videoActions']['menuRenderer']['topLevelButtons'][0]['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label'] # "No likes" or "###,###"

  #  likes_label = videoPrimaryInfoRenderer['videoActions']['menuRenderer']['topLevelButtons'][0]['toggleButtonRenderer']['accessibilityData']['label']


