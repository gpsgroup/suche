'''
   Plugin Name: Temperature
   Shows Output: Yes
   
'''
import urllib.parse
import urllib.request
import json
class Temperature:
    
    def __init__(self,city,privateKey):
        self.privateKey="20225241060860605969932890806359988880978651325956889702404168302241179833249" # keep this in app
        self.city=city
        self.privateKeySent=privateKey
         
    def run(self):
       
        url='http://api.openweathermap.org/data/2.5/weather?q='+self.city
        
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        data=response.read()
        strOut=data.decode("utf-8")
        decodedJson=json.loads(strOut)
        if(decodedJson["cod"]!='404'):            
            temp=decodedJson['main']['temp']
            temp=temp-273.15
            return str(temp)
        else:
            return ('err')
    def getPrivateKey(self):
        return self.privateKey