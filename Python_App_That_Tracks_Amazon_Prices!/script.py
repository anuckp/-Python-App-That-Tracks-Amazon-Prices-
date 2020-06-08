import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.in/gp/product/B07G4C6VM5?pf_rd_r=GJ0JDWH317HTRGG0QPXD&pf_rd_p=649eac15-05ce-45c0-86ac-3e413b8ba3d4'

headers = { "user=Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

page = requests.get(url,headers=headers)