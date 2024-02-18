import requests
from bs4 import BeautifulSoup
response=requests.get("https://appointmenttrader.com/money-network")
if response.status_code == 200:
    # Extraire le contenu de la réponse
    html_content = response.text

    # Analyser le contenu HTML
    soup = BeautifulSoup(html_content, 'html.parser')

element = soup.find_all('span', {'data-listcontainerid': 'HighestConvertingVenues'})
for each_element in element:
    print(each_element.text)
# print(element.text)