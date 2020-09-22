import requests
import json

test_id = "<INSERT TEST_ID"

te_endpoint = "https://api.thousandeyes.com/v6/web/http-server/" + test_id + ".json?headers=1&certificates=1"

payload = {}

headers = {
  'Authorization': 'Bearer <INSERT BEARER TOKEN>'
}

r = requests.request("GET", te_endpoint, headers=headers, data = payload)


r = json.loads(str(r.text))

x = 0

tests = {}

while x < len(r['web']['httpServer']):
    agent = {}
    agentName = r['web']['httpServer'][x]['agentName']
    agent['throughput'] = r['web']['httpServer'][x]['throughput']
    agent['responseTime'] = r['web']['httpServer'][x]['responseTime']
    agent['waitTime'] = r['web']['httpServer'][x]['waitTime']
    x += 1
    testData[agentName] = agent

print(json.dumps(testData))
