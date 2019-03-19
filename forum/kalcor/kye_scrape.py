from bs4 import BeautifulSoup
import requests as re
import pandas as pd

import re as regex

def kalcor_scrape():
    url = 'https://forum.sa-mp.com/member.php?u=3'

    response = re.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    body = soup.select_one('.statistics_group').text
    post_count = regex.search('([0-9])+', body).group()

    return int(post_count)