import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.in/dp/B07X1KT6LF/ref=pc_mcnc_merchandised-search-12_?pf_rd_s=merchandised-search-12&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=R4Z0WKWY5DXXYTNX6G2B&pf_rd_p=ef3e8433-f3a5-47a8-bd29-26cf72fa0567'

headers = { "user=Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

page = requests.get(url,headers=headers)

soup = BeautifulSoup(page.content,'html.parser')

title = soup.find(id="productTitle").get_text()

print(title.strip())