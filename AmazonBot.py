import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.amazon.in/gp/product/B01ELNPG2I/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1")
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
# Finding by id
s = soup.find
 

 
print(content)