import requests
import json
import urllib.request


#1. Darbs ar Placegoat API
response =requests.get("http://placegoat.com/200/200")
print(response.status_code)
print(response)
print(response.headers)

#Iegūt faila tipa nosaukumu pēc headers nosaukuma ar un bez get() funkcijas
#print(response.headers.get("Content-Type"))
#print(response.headers["Content-Type"])

#Pēc tam, kad uzzināts faila tips ieraksta to atbilstoša failu tipa failā
file = open("goat.html", "wb") #write bytes
file.write(response.content)
file.close()


#2. Darbs ar Random User
users = requests.get("https://randomuser.me/api/")
#print(users.headers)
#Atbilstoši API dokumentācijai(https://randomuser.me/) zināms,
#lai sameklētu sievietes ar Francijas pilsnonību ir jālieto key gender un nat ar atilstošiem parametriem

#HTTP metodes, https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
print(requests.delete('https://randomuser.me/api/1)'))
print(requests.options('https://randomuser.me/api/'))

#Datu atlase
query_params = {"gender": "male", "nat": "US"}
results = requests.get("https://randomuser.me/api/", params=query_params).json()
#print(results)
#Pilna URL veidošana, tas pats rezultāts
results = requests.get("https://randomuser.me/api/?gender=female&nat=fr").json()
#Izpētot atgrieztā JSON uzbūvi var piekļūt atsevišķām vērtībām
name = results['results'][0]['name']['first']
img_url = results['results'][0]['picture']['large']
print(img_url)

#3. Randomuser rezultātu ierakstīšana datnēs
#JSON formātam var izmantot dict funkcijas 
if "fr" or "FR" in results:
#print(results)
#Ieraksta rezultātus JSON failā ar append tiesībām. dump() ar papildu argumentiem iespējams realizēt pretty JSON
  with open('francuzietes.txt', 'a') as txt_file:
    json.dump(results, txt_file, indent=6, separators=(";", " = "), sort_keys=True)
    print(name+" joined our French club!")
  with open('francuzietes.json', 'a') as json_file:
    json.dump(results, json_file)

    
img_name = name +".jpg"  
urllib.request.urlretrieve("https://randomuser.me/api/portraits/women/73.jpg", img_name)
 

