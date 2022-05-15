from youtubesearchpython import VideosSearch
import gspread

gc = gspread.service_account(filename='webscrapingurls-8c796a18ea3a.json')
sh = gc.open("VideosYoutube")
worksheet = sh.get_worksheet(0)

def getVideos(topic, limit):
    buscar = topic
    videosSearch = VideosSearch(buscar, limit = limit)
    lista=[]
    count=0
    while count != (limit+1):

        videosSearch.result()['result'][count]['id']
        count = count+1

getVideos('python',10)