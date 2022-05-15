from youtubesearchpython import VideosSearch
import gspread

gc = gspread.service_account(filename='webscrapingurls-8c796a18ea3a.json')
sh = gc.open("ComentariosyLikes")
worksheet = sh.get_worksheet(0)

def getVideos(topic):
    buscar = topic
    num=10
    videosSearch = VideosSearch(buscar, limit = num)
    lista=[]
    count=0
    while count != (num):

        lista.append(videosSearch.result()['result'][count]['id'])
        count = count+1
    return lista

vi1=getVideos('python')
vi2=getVideos('java')
vi3=getVideos('machine learning')
vi4=getVideos('uipath')
vi5=getVideos('estadistica')
vi6=getVideos('data science')
vi7=getVideos('web scraping')
vi8=getVideos('desarrollo web')
vi9=getVideos('bases de datos')
vi10=getVideos('java script')
vi11=getVideos('css')
vi12=getVideos('matlab')
vi13=getVideos('programacion en R')
vi14=getVideos('visual estudio code')
vi15=getVideos('analisis de datos')
vi16=getVideos('postgre sql')
vi17=getVideos('oracle sql')
vi18=getVideos('c++')
vi19=getVideos('analisis de sentimentos')
vi20=getVideos('futbol')

vi2.extend(vi1)
vi3.extend(vi2)
vi4.extend(vi3)
vi5.extend(vi4)
vi6.extend(vi5)



ente=3
carac='C'
for vi in vi6:
    worksheet.update(carac+f'{ente}',vi)
    ente=ente+1
