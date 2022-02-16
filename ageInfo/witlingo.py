import requests
import json

# baseAPI =  "https://splicesoftware.witlingo.com"
# sessionAPI =  baseAPI + "/api/v1/sessions"
# sessionUpdateAPI = baseAPI + "/api/v1/session/0"
# requestAPI = baseAPI + "/api/v1/session/0/requests"
# methodTo = "POST"

skillToken = '005ce9c93e1b3d822c71c706b1c01ba6b6ffb8ef'
head = {'X-AUTH-TOKEN': '005ce9c93e1b3d822c71c706b1c01ba6b6ffb8ef', 'Content-Type': 'application/json'}
myUrl = 'https://splicesoftware.witlingo.com/api/v1/sessions'

def analytics(payload):

    response = requests.post(myUrl, headers=head, data=json.dumps(payload))

#2022