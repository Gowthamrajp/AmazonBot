import requests
from bs4 import BeautifulSoup

url="https://www.amazon.in/AmazonBasics-VCS35B15K-C-1-5-Litre-Bagless-Cylinder/dp/B07H3N8RJH?ref=dlx_66377_sh_dcl_img_1_23419dae_dt_mese3_9c"
headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
        }
 #Scrapping the Website data into soup
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content,'html.parser')

#Cleaning the Website data into Name and Product 
rawName = soup.find(id="productTitle")
prodName=rawName.get_text().strip()

rawPrice=soup.find_all("span", class_="a-price-whole")[0].get_text()
cleanPrice = ''.join((x for x in rawPrice if x.isdigit()))
prodPrice=(float(cleanPrice))


print(prodName)
print(prodPrice)