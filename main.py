# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

###################################################

import requests
import bs4
url='https://www.pricestday.com/2021/12/eg-bus-ticket-prices.html'
response=requests.get(url)
# this under for check that respnse got the link and it is working or you did a request for url
if(response.status_code==200):
    #transformation the response to BeautifulSoup
    #  html.parser  =  html codes

    soup=bs4.BeautifulSoup(response.content,'html.parser')

    element1 = soup.select('div h1')
    print(element1)

    element2= soup.select('div b')
    print(element2)

    print ("أسعار تذاكر إيجي باص من القاهرة إلى أسيوط ")
    element3 = soup.select('tbody tr th')
    print(element3)

    element4 = soup.select('tbody tr td')
    print(element4)

    print("اسعار تذاكر إيجي باص من القاهرة إلى المنيا")
    element5 = soup.select('tbody tr')
    print(element5)

    print("أسعار تذاكر إيجي باص من القاهرة إلى سوهاج")
    element6 = soup.select('div div table tbody tr')
    print(element6)
#this under to know what is the problem or where
else:
    print(response.status_code)




'''
    element3 = soup.select('tbody tr th')
    for h in element3:
        if('محطة القيام ' in h):
            print(element3)
        else:
            print('not found')
    print(h)"""
'''




