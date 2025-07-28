import os
import requests as req
import json

class TBA:
    def __init__(self):
        self.url = 'https://www.thebluealliance.com/api/v3/'
        self.path = self.path = os.path.dirname(os.path.abspath(__file__))
        
        self.headers = json.load(os.path.join(self.path, 'headers.json'))
        
    