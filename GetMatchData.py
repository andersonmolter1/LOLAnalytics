import requests
import json
dataRequest = requests.get('https://na1.api.riotgames.com/lol/match/v4/timelines/by-match/3008888833?api_key=RGAPI-4c01dd81-4dc2-4ce8-9d0a-716b12124110')
matchData = dataRequest.text
matchData = json.loads(matchData)
for i in 
with open('sample.json', 'w') as outfile:
        json.dump(matchData, outfile)
