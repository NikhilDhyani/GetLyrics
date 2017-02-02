import requests
import re
import webbrowser
import os

from bs4 import BeautifulSoup

flag=0
name  = (raw_input("please enter the name to search\n>"))

response = requests.get("https://www.google.co.in/search?&q="+name+"lyrics")

if response.status_code==200:
    data = response.text
    soup = BeautifulSoup(data,"html.parser")
    #print(data)
    for x in soup.find_all("h3",{"class":"r"}):        	 
        if flag==0:
           for link in x.find_all('a'):
               #print(link)
               y=link.get('href')
            
               if re.search(r'http://www.metrolyrics.com/',y):
                  flag=1
                  s = y
                  start = s.find('q=')+2
                  end = s.find('&sa', start)
                  url_extract = s[start:end]
                  

                  response = requests.get(url_extract)
               
                  data = response.text
                  soup = BeautifulSoup(data,"html.parser")
                  
                
                  for div in soup.find_all('div',{"class":"js-lyric-text"}): 
                    
                      for p in soup.find_all("p",{"class":"verse"}):  
                         print("\n")
                         print(p.getText())
               if re.search(r'http://www.lyricsmint.com/',y):
                  flag=1
                  s = y
                  start = s.find('q=')+2
                  end = s.find('&sa', start)
                  url_extract = s[start:end]
                  

                  response = requests.get(url_extract)
               
                  data = response.text
                  soup = BeautifulSoup(data,"html.parser")
                  
                
                  for div in soup.find_all('div',{"id":"lyric"}): 
                    
                      for p in div.find_all("p"):  
                         print("\n")
                         print(p.getText())
         
               if re.search(r'http://www.lyricsted.com/',y):
                  flag=1
                  s = y
                  start = s.find('q=')+2
                  end = s.find('&sa', start)
                  url_extract = s[start:end]
                  

                  response = requests.get(url_extract)
                
                  data = response.text
                  soup = BeautifulSoup(data,"html.parser")
                  
                  for div in soup.find_all('div',{"class":"entry-content group"}): 
                    
                      for p in div.find_all("p"):  
                          text=p.getText()
                          if not re.search(r'lyrics',text):
                             print("\n")
                             print(p.getText())                                
               
