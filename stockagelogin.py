import tls_client

session = tls_client.Session(client_identifier="chrome_117", random_tls_extension_order=True)

session.headers = {
    # "authority": "mystoragedata.fr",
    # "method": "POST",
    # "scheme": "https",
    "path": "/api/user/login",
    # "content-length": "257",
    "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
    "content-type": "multipart/form-data",
    
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "sec-ch-ua-platform": '"Windows"',
    "accept": "*/*",
    "sec-gpc": "1",
    "accept-language": "fr-FR,fr;q=0.8",
    "origin": "https://mystoragedata.fr",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://mystoragedata.fr/login",
    "accept-encoding": "gzip, deflate, br"
}

def login(email=...,mdp=...):
    session.get("https://mystoragedata.fr/login")
    payload="""Content-Disposition: form-data; name="email"

ilex539@gmail.com

Content-Disposition: form-data; name="password"

Alex-2003
"""



    reponse=session.post("https://mystoragedata.fr/api/user/login",json=payload)
    print(reponse.status_code)
    
login()