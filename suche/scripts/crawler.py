import time
import urllib.parse
import urllib.request

def run():
    time.sleep(1)
    url='127.0.0.1:8000/crawler/crawlpage'
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    strOut= response.read()
    print(strOut.decode("utf-8"))
    