import json
from urllib import urlopen
'''
An API that gives the continent and country name based on the ip address given
'''
url = ("http://ipvigilante.com/197.237.29.140/full")
response = urlopen(url)
'''
The api picks data from the url and responds with the corresponding data
'''
data = response.read()
data = json.loads(data)


print("Continent name: " + str(data["data"]["continent_name"]))
print("Country name: " + str(data["data"]["country_name"]))
