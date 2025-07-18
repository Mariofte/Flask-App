import requests

API_URL = "https://www.thebluealliance.com/api/v3/event/2025casj/matches"
headers = {'X-TBA-Auth-Key': 'TU_CLAVE'}
resp = requests.get(API_URL, headers=headers)
datos = resp.json()
for match in datos:
    print(match['key'], match['comp_level'], match['score_breakdown'])