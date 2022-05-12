from socket import timeout
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs # importar bs

# url de video
video_url = "https://www.youtube.com/results?search_query=python"
# sesion de html
session = HTMLSession()
# obtener el contenido html
response = session.get(video_url)
# ejecutar js
response.html.render(sleep=1,timeout=60)
# crear el objeto beautsoup
soup = bs(response.html.html, "html.parser")
#almacenar urls
videos={}
videos["link"]= soup.find_all("a", id="video-title",href=True)["href"]
print(videos)
"""
for blockquote in blockquote_items:
    autor = blockquote.find(class_='url').text
    print([autor])
    """
