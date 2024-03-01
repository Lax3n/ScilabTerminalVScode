import requests
import fake_useragent
import json

ua=fake_useragent.UserAgent()

header = {'User-Agent': ua.random,"Content-Type":"application/json",
          "Cookie":"uCke=lo=DFyyr06XGtyG%2BMslj1LkffJkKqJhgIeI4d64RDdmU4M%3D&em=DFyyr06XGtyG%2BMslj1LkffJkKqJhgIeI4d64RDdmU4M%3D&gpid=8XpDy%2FyGiZytUNvtAjMXWw%3D%3D&gid=120208699912&l=1&t=3; authCke=atk=717e26ba-eddd-4329-a8b8-ee2309cece2b&rtk=&tks=CONSUMER&tkt=bearer&eik=1209600&tcd=2024-02-18T22%3A05%3A25.741Z&atke=2024-03-03T22%3A05%3A25.741Z; otuvid=C1592442-8A23-451B-BD87-F1838A59BA9D; ha_userSession=lastModified=2024-02-22T12%3A59%3A05.000Z&origin=prod-sc; OT-SessionId=cad7ea03-9bda-4186-a282-ab752ea3e00c; OT_dtp_values=datetime=2024-03-01 12:00; __stripe_mid=d21d82e0-0600-45c5-9b19-03a08e1601fa456056; __stripe_sid=feb1c316-cd33-4a22-ba9d-f4062fafa2d676e520; OT-Locale=en-US; ak_bmsc=CE189EAC7F8A9822984C435B3C158A1E~000000000000000000000000000000~YAAQwDwSAiAqfe6NAQAANrIR9xa8Mz7tIkV7u+K29lnAklNQfUAx1UyqAr6KbAfVxWk3qc6xX3bTMXTXeA/pMwp9q4gevNbg5LBC6VHo+g2zW81iqz5ANqriSLp+lHp2XQOlB7TC5FW/b9Lou6Q0oC6c4yM92iMder7Pt8uvP6/LLFWWlfN379VnLshWcfmmfPm+RggfwzoS08Kwr+QBQ23ptzVsYd9axEJMj6BQrnEsKagPZEF7fS+iMQ1m2TbyFJa7Ioc4En35aPvkhaYRBlzBSyWs3/YhCUnDXjbCjD+AHNbFBF10RrZcpsgSs/K5Yk2L+jounckuKbv/YbxP0cozZr9eEEUsk67VgAlQpiFok3MwrvNtvkgvymzxpzBSeod80G8sLUen+/yzDrI=; 1ac135e65c782b51_cfid=3f471h070639642224086cb02d3a7i907e1d939g4049bj9ec70d391b9d96716b2d7eb7b39681615155cc0gah8a52b4018jb49e0h8h135j2d604abfa0a5306650; 1ac135e65c782b51_cffid=588516c5526ga4746h5e64ai7743ca201d12804i2e284456638g8f1h5h5f6h7eb9965cb696a8b14e6b6hai1g93c606a40f4d39978d091cc1b82e555jc6253957; bm_mi=67F7A614E97BCA6066D55D314F60C956~YAAQwDwSAsUtfe6NAQAAmz0T9xY+leJlW1oisedRcs4I5A1KGizO5JQBHy5nMvdEZNTCFGrQApYVO8U+Kg0FFtY0WCXAjX3ixfqgEs+mwfd+xtVMB9Tgz5lRuFE3jfFGoxJ7Ki/+WhihibXGv+U6yzSSoDxCcPrnc80Nh+w9qSC5rVlIC5tn7NuL3DbZgvHmR1mAnYNxKh6+NxL78SiMd49rhkwV65wfDkpdGm2K120NQwlRcmE5GuvJ+NmIh0xQGM26yfOffSqU4q/bim013tAuG5slmLSDj6q/Yeka2RccmxD3cobpuN43f4DTfJhJ9rb3gTUch106c3miQ67GhYQZlbKrXetaeUc=~1; ftc=x=2024-02-29T23%3A54%3A13&c=1&pt1=1&pt2=1&rf1=1068&rf2=1068&er=1268701&p1ca=restaurant%2Fprofile%2F1279777&p1q=ref%3D1068; OT-Session-Update-Date=1709247259; bm_sv=44EEF0C320D5343C4064508652B16A29~YAAQwDwSAk8ufe6NAQAA+2QT9xZB8QRp8VGm8DRi2MjjONWXA8mvsPzfJn+a2cw9Nt68TSXn2lwOGuL8rfUGqtzhUwvCHXRFXd3CJaN0MSB4LQpsJjVzhbDXVbgWw2aHBip1uD9qI3icyQKCEvlSmg8+m3BXTT7zMbLOkGccW2o2ABmaDuXz8v9tfbmO/JeYe8qiYU7za7Ej49p982D5EOzOFh/s9M2BwJ5CdVUDakyLorOcCVi4wRZGpEqVnGXMSHqvCA==~1",
          'X-Csrf-Token': 'e1782c47-8a29-4254-9b40-9ee39038db45'}
def makePayload():
    reponse=requests.get("")


def creationsession():
#     reponsesession=requests.post("https://www.opentable.fr/dapi/v1/session",headers={'User-Agent': ua.random ,'Accept': '*/*',
# "Accept-Encoding": 'gzip, deflate, br',
# "Accept-Language": 'fr-FR,fr;q=0.5',
# "Connection": 'keep-alive',
# "Content-Length": 0,
# "Cookie": 'ha_userSession=lastModified=2024-02-22T12%3A59%3A05.000Z&origin=prod-rs; otuvid=BACBB823-D542-497B-82C6-D1789CB9F3AB; OT-SessionId=f2f417bb-ecd1-4fb8-98e4-0b2fe68a25ea; OT_dtp_values=datetime=2024-03-01 12:00; ha_userSession=lastModified=2024-02-22T12%3A59%3A05.000Z&origin=prod-rs; __stripe_mid=ef36ba70-c6bb-4430-909d-22c5483757290547b0; __stripe_sid=11dc2680-2443-42b9-801c-b2b6f9d3d944042e14; ftc=x=2024-03-01T00%3A32%3A39&c=1&pt1=1&pt2=1&er=1268701; OT-Session-Update-Date=1709249560',
# "Host": 'www.opentable.fr',
# "Origin": 'https://www.opentable.fr',
# "Referer": 'https://www.opentable.fr/',
# "Sec-Fetch-Dest":' empty',
# "Sec-Fetch-Mode": 'cors',
# "Sec-Fetch-Site": 'same-origin',
# "Sec-GPC": 1,
# "x-csrf-token": '04c63d40-2e78-42ac-bbef-706ec0116448'})
    reponsesession=requests.post("https://www.opentable.fr/dapi/v1/session")
    return reponsesession.json()

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
