import requests
import json
dataRequest = requests.get('https://na1.api.riotgames.com/lol/match/v4/timelines/by-match/3008888833?api_key=RGAPI-187e7282-6283-4d1b-915f-66479d618862')
matchData = dataRequest.text
matchData = json.loads(matchData) 
with open('sample.json', 'w') as outfile:
        json.dump(matchData, outfile)
