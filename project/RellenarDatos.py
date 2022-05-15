from xml.etree.ElementTree import canonicalize
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs # importar bs
from googleapiclient.discovery import build
import requests
import gspread
import json
import re


gc = gspread.service_account(filename='webscrapingurls-8c796a18ea3a.json')
sh = gc.open("ComentariosyLikes")
worksheet = sh.get_worksheet(0)
fcom='D'
flik='E'

api_key ="AIzaSyCFynPLwBDrOk6oo5zQUYtWcjLagwVbBr8"
resource = build('youtube', 'v3', developerKey=api_key)

aux=True
fila=34
while aux:
    video_id=worksheet.acell('C'+f"{fila}").value
    url="https://returnyoutubedislikeapi.com/votes?videoId="+video_id

    response=requests.get(url).text
    json_data=json.loads(response)

    worksheet.update(flik+f"{fila}", json_data['likes'])

    request = resource. videos().list(part="statistics",
                                        id=video_id)
    #execute the request
    response =request.execute()
    
    worksheet.update(fcom+f"{fila}", response['items'][0]['statistics']['commentCount'])

    fila=fila+1
    aux1=worksheet.acell('c'+f"{fila}").value
    if(aux1 == None):
        aux=False

