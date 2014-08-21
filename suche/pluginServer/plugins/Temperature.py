'''
   Plugin Name: Temperature
   Shows Output: Yes
   
'''
import urllib.parse
import urllib.request
import json
class Temperature:
    
    def __init__(self,city,privateKey):
        self.privateKey="52364956476270096215486697602522302207783308911809137141918051922786023308176" # keep this in app
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
            temp=round(temp,2)
            op='<div class="resultBox"><div class="col-md-9"><div class="row"><div class="col-md-12"><span class="helvnu">'+str(temp)+' &deg;C</span></div></div><div class="row"><div class="col-md-12">Temperature of '+self.city.title()+','+decodedJson['sys']['country']+'</div></div></div> <div class="col-md-3"></div></div>'
            return (op)
        else:
            return ('err')
        
    def getPrivateKey(self):
        return self.privateKey
