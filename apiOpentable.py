import requests
import fake_useragent
import json

ua=fake_useragent.UserAgent()

# header = {'User-Agent': ua.random,"Content-Type":"application/json",
#           "Cookie":"ftc=x=2024-03-01T10%3A40%3A21&c=1&pt1=1&pt2=1; otuvid=1306F78F-90B2-4E68-B5CD-4F14C4E1D846; OT-SessionId=eeb293e5-dd04-4b34-a7dd-a8e57817f565; OT-Session-Update-Date=1709286022; ha_userSession=lastModified=2024-02-22T12%3A59%3A05.000Z&origin=prod-rs",
#           'X-Csrf-Token': '6fbdb46f-b99a-4990-b2d1-e51872bff401'}


def creationsession():
    reponsesessionid=requests.post("https://www.opentable.fr/dapi/fe/proxy/consumer-frontend/trackgoal")
    headers=dict(reponsesessionid.headers)
    print(headers)
    otuvid=headers["Set-Cookie"]
    
    header = {'User-Agent': ua.random,"Content-Type":"application/json",
          "Cookie":f"ftc=x=2024-03-01T10%3A40%3A21&c=1&pt1=1&pt2=1; otuvid={otuvid}; OT-SessionId={sessionId};"}
    
    reponseget=requests.get("https://cdn.otstatic.com/cfe/14/js/home-K6ITR4D6.js",headers={"Content-Type":"application/json"})
    print(reponseget.status_code)
    sha256=reponseget.text.split("documentId")[1].split('"')[1]
    payload={"operationName":"HomeModuleLists","extensions":{"persistedQuery":{"sha256Hash":sha256,"version":1}}}
    
    reponsepost=requests.post("https://www.opentable.fr/dapi/fe/gql?optype=query&opname=HomeModuleLists",headers=header, data=payload)
    print(reponsepost.status_code)
    

def reservation(restaurantID:int=...):
    payload = {
        "additionalServiceFees": [],
        "attributionToken": "x=2024-02-29T23%3A17%3A09&c=1&pt1=1&pt2=1&rf1=1068&rf2=1068&er=1268701&p1ca=restaurant%2Fprofile%2F1279777&p1q=ref%3D1068",
        "correlationId": "6176139e-cb26-419d-ac3e-93a63f527cc2",
        "country": "US",
        "dinerIsAccountHolder": True,
        "diningAreaId": 1,
        "email": "alexandre.sage@outlook.fr",
        "firstName": "Alexandre",
        "gpid": 120208699912,
        "isModify": False,
        "katakanaFirstName": "",
        "katakanaLastName": "",
        "lastName": "SAGE",
        "nonBookableExperiences": [],
        "optInEmailRestaurant": True,
        "partySize": 2,
        "phoneNumber": "638054871",
        "phoneNumberCountryId": "FR",
        "points": 100,
        "pointsType": "Standard",
        "reservationAttribute": "default",
        "reservationDateTime": "2024-03-01T12:00",
        "reservationType": "Standard",
        "restaurantId": 1268701,
        "slotAvailabilityToken": "eyJ2IjoyLCJtIjowLCJwIjowLCJjIjo2LCJzIjowLCJuIjowfQ",
        "slotHash": "885423000",
        "slotLockId": 761932273,
        "tipAmount": 0,
        "tipPercent": 0
    }
    reponse = requests.post("https://www.opentable.com/dapi/booking/make-reservation",headers=header,data=json.dumps(payload))
    return (reponse.status_code, reponse.json)


print(creationsession())
