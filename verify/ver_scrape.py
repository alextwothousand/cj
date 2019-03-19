from bs4 import BeautifulSoup
import requests as re

def verify_scrape(id):
    url = f'https://forum.sa-mp.com/member.php?u={id}'

    response = re.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    body = soup.select_one('.profilefield_category').text
    text = body.splitlines()
    
    return text[4]
