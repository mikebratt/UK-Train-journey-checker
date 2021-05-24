import requests
from bs4 import BeautifulSoup
import json
import http.client, urllib

destination = 'HDG'
origin = 'MCO'
departure = '1710'

url = ('http://ojp.nationalrail.co.uk/service/timesandfares/' + origin + '/' + destination + '/today/' + departure + '/dep')

status = json.loads(str(BeautifulSoup(requests.get(url).content, 'html.parser').find('script', id='jsonJourney-4-1'))[56:-9])["jsonJourneyBreakdown"]["statusMessage"]

if not 'on time' in status:
   conn = http.client.HTTPSConnection("api.pushover.net:443")
   conn.request("POST", "/1/messages.json", urllib.parse.urlencode({
       "token": "xxxxxxxxxxxxxxxxxxxxx", "user": "xxxxxxxxxxxxxxxxxxxxx",
       "message": "Train " + status + " " + url ,
       "sound": "falling", "priority": 1,
     }), { "Content-type": "application/x-www-form-urlencoded" })
   conn.getresponse()
