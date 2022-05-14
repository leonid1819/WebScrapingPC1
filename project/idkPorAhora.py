import requests
import json
import re

video_id="1uAH93tzfQY"
url="https://returnyoutubedislikeapi.com/votes?videoId="+video_id
response=requests.get(url).text
json_data=json.loads(response)

print(json_data['likes'])