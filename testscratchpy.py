import tls_client
import time
from urllib.parse import quote

date_formattee = time.strftime("%Y-%m-%dT%H:%M:%S")

formatted_time = quote(date_formattee)
print(formatted_time)



def reservation():
    session=tls_client.Session(client_identifier="1",random_tls_extension_order=True)
    session.headers={
        "path": "/",
        "scheme": "https",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "fr-FR,fr;q=0.7",
        "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Sec-Gpc": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    # session.execute_request("GET","https://www.opentable.com")
    # print(vars(session))
    payload = {"pageGroup":"booking",
               "pageType":"network_details",
               "dagEvent":{"timestamp":"2024-03-03T16:33:00Z","checkoutType":"reservation","checkoutDetails":{"rid":191058,"partySize":2,"reservationDatetime":"2024-03-21T18:00:00.000Z"},
                           "requestId":"562594fd-3a15-451b-b92d-e38ada498dee",
                           "context":{"app":{"name":"consumer-frontend","platform":"web","locale":"en-US"}}}}


    # print(session._session_id)
    # response=session.execute_request(method="GET",url=f"https://www.opentable.com/s?dateTime={formatted_time}&covers=2&ridsAddons%5B%5D=1268701&latitude=40.7685526&longitude=-73.9831866&shouldUseLatLongSearch=true",data=payload)
    response=session.execute_request(method="POST",url=f"https://www.opentable.com/r/bad-roman-new-york?corrid=b4fea431-8ab9-4b0f-a094-5862c6616752&avt=eyJ2IjoyLCJtIjowLCJwIjowLCJzIjowLCJuIjowfQ&p=2&sd=2024-03-03T19%3A00%3A00",json=payload)
    
    
    # print(vars(response))
    
    reponse=session.execute_request(method="POST",url="https://www.opentable.com/dapi/booking/make-reservation",json=payload)
    print(reponse.status_code)
    # print(vars(session))
    
reservation()