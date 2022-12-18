import requests
from bs4 import BeautifulSoup
import pandas as pd
Product_name=[]
Prices =[]
Description = []
Reviews = []


url ="https://www.flipkart.com/search?q=mobile+under+50000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_2_14_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_2_14_na_na_na&as-pos=2&as-type=RECENT&suggestionId=mobile+under+50000&requestId=ef3ed01b-b72f-4b23-9573-64c16c98d386&as-searchtext=mobile+under+5&page=1"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
soup1 = soup.find("div",class_="_1YokD2 _3Mn1Gg")


names = soup1.find_all("div",class_= "_4rR01T")
for i in names:
    name = i.text
    Product_name.append(name)



prices = soup1.find_all("div",class_= "_30jeq3 _1_WHN1")
for i in prices:
    name = i.text
    Prices.append(name)

desc = soup1.find_all("ul",class_="_1xgFaf")
for i in desc:
    name= i.text
    Description.append(name)


reviews= soup1.find_all("div",class_="_3LWZlK")
for i in reviews:
    name = i.text
    Reviews.append(name)


df = pd.DataFrame({"Product Name":Product_name,"Prices":Prices,"Description":Description,"Reviews":Reviews})
#print(df)
df.to_csv("C:/Users/hp/Desktop/WebScrap/flipkart_mobile_under_50000.csv")









