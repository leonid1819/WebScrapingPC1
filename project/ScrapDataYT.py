from xml.etree.ElementTree import canonicalize
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs # importar bs
from googleapiclient.discovery import build
import requests
import gspread
import json
import re


gc = gspread.service_account(filename='webscrapingurls-8c796a18ea3a.json')
sh = gc.open("VideosYoutube")
worksheet = sh.get_worksheet(0)
ftit='C'
fdesc='E'
fcana='F'
flike='G'
fdislk='H'
fcomm='I'


api_key ="AIzaSyCFynPLwBDrOk6oo5zQUYtWcjLagwVbBr8"
resource = build('youtube', 'v3', developerKey=api_key)

def getShadowLikes(video_id,worksheet,fila):
    url="https://returnyoutubedislikeapi.com/votes?videoId="+video_id
    response=requests.get(url).text
    json_data=json.loads(response)
    worksheet.update(flike+f"{fila}", json_data['likes'])


def getShadowDislikes(video_id,worksheet,fila):
    url="https://returnyoutubedislikeapi.com/votes?videoId="+video_id
    response=requests.get(url).text
    json_data=json.loads(response)
    worksheet.update(fdislk+f"{fila}", json_data['dislikes'])


def getComentarios(video_id,worksheet,fila):
    request = resource. commentThreads().list(
                            part="snippet",
                            videoId=video_id,
                            maxResults= 10,   
                            order="orderUnspecified")  
   
    response =request.execute()

     
    items = response["items"][:10]
    total=""
    for item in items:
        item_info = item["snippet"]
        
       
        topLevelComment = item_info["topLevelComment"]
        comment_info = topLevelComment["snippet"]
        total=total+comment_info["textDisplay"]+"{comentario}"
    total=total+"axuliar"
    worksheet.update(fcomm+f"{fila}", total)



def getData(video_id,worksheet,fila):

    url="https://www.youtube.com/watch?v="+video_id


    session = HTMLSession()

    response = session.get(url)

    response.html.render(sleep=1,timeout=60)

    soup = bs(response.html.html, "html.parser")

    titulo=soup.find("meta", itemprop="name")["content"]
    descripcion=soup.find("meta", itemprop="description")['content']
    canal=soup.find("span", itemprop="author").next.next['content']
    data = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)
    data_json = json.loads(data)
    videoPrimaryInfoRenderer = data_json['contents']['twoColumnWatchNextResults']
    ['results']['results']['contents'][0]['videoPrimaryInfoRenderer']
    videoSecondaryInfoRenderer = data_json['contents']
    ['twoColumnWatchNextResults']['results']['results']['contents'][1]
    ['videoSecondaryInfoRenderer']
    
    likes_label_aux = videoPrimaryInfoRenderer['videoActions']
    ['menuRenderer']['topLevelButtons'][0]['toggleButtonRenderer']
    ['accessibilityData']['accessibilityData']['label']
    if likes_label_aux == "Me gusta":
        getShadowLikes(video_id,worksheet,fila)
    else:
        likes_label = videoPrimaryInfoRenderer['videoActions']['menuRenderer']
        ['topLevelButtons'][0]['toggleButtonRenderer']['defaultText']
        ['accessibility']['accessibilityData']['label'] 
        likes_str = likes_label.split()[0].replace(',','')
        likes= '0' if likes_str == 'No' else likes_str
        worksheet.update(flike+f"{fila}", int(likes))
   
    
    worksheet.update(ftit+f"{fila}", titulo)
    worksheet.update(fdesc+f"{fila}", descripcion)
    worksheet.update(fcana+f"{fila}", canal)
    


def scraping(filaI,worksheet):
    
    aux=True
    while aux:
        video_id=worksheet.acell('D'+f"{filaI}").value
        getShadowDislikes(video_id,worksheet,filaI)
        getComentarios(video_id,worksheet,filaI)
        getData(video_id,worksheet,filaI)
        filaI=filaI+1
        aux1=worksheet.acell('D'+f"{filaI}").value
        if(aux1 == None):
            aux=False

scraping(3,worksheet)


