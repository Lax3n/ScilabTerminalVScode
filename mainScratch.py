import tls_client
import uuid
import time
import urllib.parse
import json

from typing import Any, Dict, List, Optional, Union


uuidcorrelationid=uuid.uuid4()
Xcsrftoken=uuid.uuid4()
# print(uuidcorrelationid)

date_formattee = time.strftime("%Y-%m-%dT%H:%M:%S")
formatted_time = urllib.parse.quote(date_formattee)


def reservation(rid:int=1268701):
    
    session=tls_client.Session(client_identifier="chrome_117",random_tls_extension_order=True)
    session.headers={
        "authority":"www.opentable.com",
        "path": "/",
        "scheme": "https",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Ot-Page-Group":"booking",
        "Ot-Page-Type":"network_detail",
        'Accept-Language' : 'fr-FR,fr;q=0.9, en-US; q=0.8, en; q=0.7',
        "Content-Type":"application/json",
        "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": 'empty',
        "Sec-Fetch-Mode": 'cors',
        "Sec-Fetch-Site": 'same-origin',
        "Sec-Fetch-User": "?1",
        "Sec-Gpc": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "dnt":"1",
        "Referer":"https://www.opentable.com/",
        "Origin":"https://www.opentable.com/"
        
    }
    
    
    # responsesha256hash=session.execute_request("GET","https://cdn.otstatic.com/cfe/14/js/chunk-UN2K5WOL.js")
    # print(responsesha256hash.status_code)
    # sha256hash=responsesha256hash.text.split("wv.documentId")[1].split('"')[1]
    
    
    # responsehome=session.execute_request("GET",f"https://www.opentable.com/")
    # print(responsehome.status_code)
    # responseinitialisation=session.execute_request("GET",f"https://www.opentable.com/s?dateTime=2024-03-10T12%3A00%3A00&covers=2&ridsAddons%5B%5D=1268701&latitude=40.7685526&longitude=-73.9831866&shouldUseLatLongSearch=true&originCorrelationId={uuidcorrelationid}")
    # print(responseinitialisation.status_code)
    starturl=f"https://www.opentable.com/booking/details?availabilityToken=eyJ2IjoyLCJtIjowLCJwIjowLCJjIjo2LCJzIjowLCJuIjowfQ&correlationId={uuidcorrelationid}&creditCardRequired=false&dateTime=2024-03-10T21%3A15%3A00&partySize=2&points=100&pointsType=Standard&resoAttribute=default&rid={rid}&isModify=false&isMandatory=false&cfe=true"
    print(starturl)
    responseSlotHash=session.execute_request("GET",starturl)
    # print(responseSlotHash.status_code)
    
    slothash=responseSlotHash.text.split('"slotHash"')[1].split('"')[1]
    
    attributiontoken=responseSlotHash.text.split('"attributionToken"')[1].split('"')[1]
    
    csrftoken=responseSlotHash.text.split('__CSRF_TOKEN__')[1].split("'")[1]
    # print(csrftoken)
    session.headers.update({"X-Csrf-Token":f"{csrftoken}"})
    # print(vars(session))
    
    
    # session.headers.update({"Referer":f"https://www.opentable.com/booking/details?availabilityToken=eyJ2IjoyLCJtIjowLCJwIjowLCJjIjo2LCJzIjowLCJuIjowfQ&correlationId={uuidcorrelationid}&creditCardRequired=false&dateTime=2024-03-10T21%3A15%3A00&partySize=2&points=100&pointsType=Standard&resoAttribute=default&rid={rid}&isModify=false&isMandatory=false&cfe=true"})
    
    
    
    #####################################################
    #
    # payloadtitou={"pageGroup":"booking",
    #               "pageType":"network_details",
    #               "dagEvent":
    #                   {"timestamp":"2024-03-03T22:21:00Z",
    #                    "checkoutType":"reservation",
    #                    "checkoutDetails":
    #                        {"rid":rid,
    #                         "partySize":2,
    #                         "reservationDatetime":"2024-03-10T21:15:00.000Z"},
    #                        "requestId":f"{uuidcorrelationid}",
    #                        "context":
    #                            {"app":
    #                                {"name":"consumer-frontend",
    #                                 "platform":"web",
    #                                 "locale":"en-US"}}}}
    
    
    # responseTitou=session.execute_request("POST","https://www.opentable.com/dapi/dag/v1/single/initcheckout",json=payloadtitou)
    # print(responseTitou.status_code)
    #
    #################################
    
    # responsefill=session.execute_request("GET","https://www.opentable.com/resources/4aba7d3860f9f5c51c02b5f1073bb474d22eb7862361e")
    # print(responsefill.status_code)
    
    
    # Xcsrftoken=responseSlotHash.text.split("__CSRF_TOKEN__")[1].split("'")[1]
    
    # session.headers.update({"X-Csrf-Token":f"{Xcsrftoken}"})
    # print(Xcsrftoken)
    # print(session)
    
    # payloadSlotLockId={
    # "extensions": {
    #     "persistedQuery": {
    #     "version": 1,
    #     "sha256Hash": f"{sha256hash}"
    #     }
    # },
    # "operationName": "BookDetailsStandardSlotLock",
    # "variables": {
    #     "slotLockInput": {
    #     "restaurantId": rid,
    #     "seatingOption": "DEFAULT",
    #     "reservationDateTime": "2024-03-10T21:15",
    #     "databaseRegion": "NA",
    #     "diningAreaId": 1,
    #     "partySize": 2,
    #     "reservationType": "STANDARD",
    #     "slotHash": f"{slothash}"
    #     }
    # }
    # }
    
    # print(vars(session))
    # session.headers.update({"path":"/dapi/fe/gql?optype=mutation&opname=BookDetailsStandardSlotLock",
    #                         "Referer":f"https://www.opentable.com/booking/details?availabilityToken=eyJ2IjoyLCJtIjowLCJwIjowLCJjIjo2LCJzIjowLCJuIjowfQ&correlationId={uuidcorrelationid}&creditCardRequired=false&dateTime=2024-03-10T21%3A15%3A00&partySize=2&points=100&pointsType=Standard&resoAttribute=default&rid={rid}&isModify=false&isMandatory=false&cfe=true",
    #                         "X-Query-Timeout":"4000"
    #                         })
    
    # responseSlotLockId=session.execute_request("POST",f"https://www.opentable.com/dapi/fe/gql?optype=mutation&opname=BookDetailsStandardSlotLock",data=payloadSlotLockId)
    # print(responseSlotLockId.status_code)
    # print(responseSlotLockId.text)
    payloadreservationuser={
        "restaurantId":1268701,
        "slotAvailabilityToken":"eyJ2IjoyLCJtIjowLCJwIjowLCJjIjo2LCJzIjowLCJuIjowfQ",
        "slotHash":"3723634056",
        "slotLockId":926420119,
        "isModify":False,
        "nonBookableExperiences":[],
        "reservationDateTime":"2024-03-30T18:45",
        "partySize":2,
        "firstName":"ninon",
        "lastName":"Charlotte",
        "email":"alexandre.sage41@gmail.com",
        "dinerIsAccountHolder":False,
        "country":"US",
        "reservationType":"Standard",
        "reservationAttribute":"default",
        "katakanaFirstName":"",
        "katakanaLastName":"",
        "gpid":190209510679,
        "correlationId":"5072fc65-4f62-4f1d-875b-f5a18ac51029",
        "attributionToken":"x=2024-03-05T21%3A35%3A22&px=1&c=1&pt1=1&pt2=1&er=1268701&p1ca=booking%2Fview&p1q=showCancelModal%3Dtrue%26rid%3D1268701%26confnumber%3D132928%26token%3D01YpkTaRT8LQj_DfOB73pvYl4CTqYymHmL6fJxT5lFf...",
        "additionalServiceFees":[],
        "tipAmount":0,
        "tipPercent":0,
        "pointsType":"None",
        "points":0,
        "diningAreaId":1,
        "phoneNumber":"638054871",
        "phoneNumberCountryId":"FR",
        "optInEmailRestaurant":False
    }
    
    
    
    
    
    
    
    payloadreservation = {
    "additionalServiceFees": [],
    "attributionToken": f"{attributiontoken}",
    "correlationId": f"{uuidcorrelationid}",
    "country": "US",
    "diningAreaId": 1,
    "email": "alexandre.sage41@gmail.com",
    "firstName": "ninon",
    "dinerIsAccountHolder":False,
    "isModify": False,
    "katakanaFirstName": "",
    "katakanaLastName": "",
    "lastName": "charlotte",
    "nonBookableExperiences": [],
    "optInEmailRestaurant": False,
    "partySize": 2,
    "phoneNumber": "638054871",
    "phoneNumberCountryId": "FR",
    "points": 100,
    "pointsType": "Standard",
    "reservationAttribute": "default",
    "reservationDateTime": "2024-03-10T21:15",
    "reservationType": "Standard",
    "restaurantId": rid,
    "slotAvailabilityToken": "eyJ2IjoyLCJtIjowLCJwIjowLCJjIjo2LCJzIjowLCJuIjowfQ",
    "slotHash": f"{slothash}",
    "tipAmount": 0,
    "tipPercent": 0
    }
    session.headers.update({"path":"/dapi/booking/make-reservation"})
    
    
    response=session.execute_request("POST","https://www.opentable.com/dapi/booking/make-reservation",json=payloadreservationuser)
    print(response.status_code)
    
reservation()
    
    
def login():
    Xcsrftokenlocal = uuid.uuid4()
    session.headers = {
        "authority": "www.opentable.com", 
        "path": "/dapi/fe/gql?optype=mutation&opname=SendVerificationCodeEmail",
        "scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "fr-FR,fr;q=0.9, en-US; q=0.8, en; q=0.7",
        "Cache-Control":"no-cache",
        "Content-Type":"application/json",
        "Origin":"https://www.opentable.com",
        "Ot-Page-Group": "user",
        "Ot-Page-Type": "authentication_start",
        "Pragma":"no-cache",
        "Referer":"https://www.opentable.com/authenticate/start?rp=https%3A%2F%2Fwww.opentable.com%2F&srs=1&isFromBookingFlow=false&isPopup=true&origin=global_heade",
        "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Gpc": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "X-Csrf-Token": f"{Xcsrftokenlocal}",
        "X-Query-Timeout":"2000"
    }
    
    # responsecookie=session.execute_request("GET","https://www.opentable.com/authenticate/start?rp=https%3A%2F%2Fwww.opentable.com%2F&srs=1&isFromBookingFlow=false&isPopup=true&origin=global_heade")
    # print(responsecookie)
    
    
    # responsecookie = session.execute_request("GET", "https://www.opentable.com/authenticate/start?rp=https%3A%2F%2Fwww.opentable.com%2F&srs=1&isFromBookingFlow=false&isPopup=true&origin=global_heade")
    # print(responsecookie.status_code)
    # session.headers.update({"X-Csrf-Token": Xcsrftokenlocal})
    # payloadmail={}
    # responsesession = session.execute_request("POST", "https://www.opentable.com/dapi/v1/session",json=payloadmail)

    # print(responsesession.status_code)
    # session.headers.update(
    #     {
    #         "method":"POST",
    #         "path": "/dapi/fe/gql?optype=mutation&opname=SendVerificationCodeEmail",
    #         "Ot-Page-Group": "user",
    #         "Ot-Page-Type": "authentication_start",
    #         "Referer": "https://www.opentable.com/authenticate/start?rp=https%3A%2F%2Fwww.opentable.com%2F&srs=1&isFromBookingFlow=false&isPopup=true&origin=global_header",
    #         "X-Csrf-Token": f"{Xcsrftokenlocal}",
    #     "X-Query-Timeout": "2000"
    #     }
    # )
    # print(vars(session))
    # with open("session.json","w") as f:
    #     json.dump(vars(session),f,indent=4)
    # session.headers.update({})
    
    
    payloademail = {"operationName":"SendVerificationCodeEmail",
                    "variables":
                        {"verifyEmail":False,
                         "email":"alexandre.sage41@gmail.com",
                         "loginType":"popup-redirect",
                         "requestedAction":"https://www.opentable.com/",
                         "path":"https://www.opentable.com/authenticate/start?rp=https%3A%2F%2Fwww.opentable.com%2F&srs=1&isFromBookingFlow=false&isPopup=true&origin=global_heade",
                         "origin":"unknown"},
                        "extensions":
                            {"persistedQuery":
                                {"version":1,
                                 "sha256Hash":"7a9ab940a239a8972a6157ace71d6885112aebf46d36592feaa828313a0eda21"}}}
    # session.headers.update({
    # "X-Query-Timeout": "2000"
    # })
    
    responsesendemail = session.post("https://www.opentable.com/dapi/fe/gql?optype=mutation&opname=SendVerificationCodeEmail",json=payloademail)
    print(responsesendemail)
    # print(vars(responsesendemail))