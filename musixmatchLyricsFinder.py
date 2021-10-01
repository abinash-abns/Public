# Package req: requests,json,bs4
import requests
import json
from bs4 import BeautifulSoup
import re

apikey = "?apikey=c7d2bcddbd2e6e855b525a65f6cb56cc&"

musicName = input("Enter song name:")
musicName = musicName.replace(" ",'%')

apikey = "?apikey=c7d2bcddbd2e6e855b525a65f6cb56cc&"
apiParams = "format=json&q_track=" + musicName

apiURL = "https://api.musixmatch.com/ws/1.1/matcher.track.get" + apikey + apiParams

response = requests.request("GET", apiURL)
res= response.text
res = json.loads(res)

trackURL = res['message']['body']['track']['track_share_url']

print(trackURL)

response = requests.request("GET", trackURL, headers={'user-agent': 'custom'})
res= response.text
soup = BeautifulSoup(res, 'html.parser')

text1 = soup.find_all("span", {"class": "lyrics__content__ok"})
print(text1)

