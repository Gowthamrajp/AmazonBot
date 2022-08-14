import requests
import os;
from bs4 import BeautifulSoup
import pandas as pd
import pywhatkit
import mysql.connector

#setting up mySQL DB 

myDb = mysql.connector.connect(
        host="localhost",
        user="gowtham",
        passwd="Pandian@65"
)
#importing links from CSV using pandas
productData = pd.read_csv (os.getcwd()+"\productData.csv")  

with open(os.getcwd()+"\WhatsAppDetails.txt") as f:
    contents = f.readline()
    content = contents[0]
if content == "+":
        flag=0
else:
        flag=1

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
                if(flag == 1):
                        pywhatkit.sendwhatmsg_to_group_instantly(contents,  "Price of "+ name +" Reduced to: "+ str(prodPrice))#+" url is "+url)
                else:
                        pywhatkit.sendwhatmsg_instantly(contents , "Price of "+ name +" Reduced to: "+ str(prodPrice))#+" url is "+url))

        print(name)
        print(prodName)
        print(prodPrice)
        productData.to_csv("productData.csv", index=False)

#scrapper function call for each product
for x in range(0,len(productData["ProductName"])):
        print(x+1)
        scrapper(productData["ProductName"][x], productData["Product Link"][x],x)

