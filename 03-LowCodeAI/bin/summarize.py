import requests
import sys

key = "<YOUR KEY HERE>"

data = {
    "key" : (None,key),
    "txt" : (None,sys.argv[1]),
    "lang" : (None,"en"),
    "sentences" : (None,1),
    "of" : (None,"json")
}

res = requests.post("https://api.meaningcloud.com/summarization-1.0",files=data)

print(res.json()['summary'])