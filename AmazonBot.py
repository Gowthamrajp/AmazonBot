import requests
from bs4 import BeautifulSoup
import pandas as pd
import pywhatkit

#importing links from CSV using pandas
productData = pd.read_csv ("productData.csv")  


headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
        }

        
def scrapper(name,url,i):
        #Scrapping the Website data into soup
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content,'html.parser')

        #Cleaning the Website data into Name and Product 
        rawName = soup.find(id="productTitle")
        prodName=rawName.get_text().strip()

        rawPrice=soup.find_all("span", class_="a-price-whole")[0].get_text()
        cleanPrice = ''.join((x for x in rawPrice if x.isdigit()))
        prodPrice=(float(cleanPrice))
        #checking price change
        if productData["lastKnownPrice"][i]>prodPrice: 
        #updating price into CSV 
                productData["lastKnownPrice"][i]=prodPrice
                pywhatkit.sendwhatmsg_instantly("+919500133791", "Price of "+ name +" changed")
        print(name)
        print(prodName)
        print(prodPrice)
        productData.to_csv("productData.csv", index=False)

#scrapper function call for each product
for x in range(0,len(productData["ProductName"])):
        print(x+1)
        scrapper(productData["ProductName"][x], productData["Product Link"][x],x)

