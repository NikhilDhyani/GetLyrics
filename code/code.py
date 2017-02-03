import requests
import re
import webbrowser
import os

from bs4 import BeautifulSoup

flag=0
name  = (raw_input("please enter the name of the song to search Lyrics\n>"))

response = requests.get("https://www.google.co.in/search?&q="+name+"lyrics")

if response.status_code==200:
    data = response.text
    soup = BeautifulSoup(data,"html.parser")
    
    for x in soup.find_all("h3",{"class":"r"}):        	 
        if flag==0:
           for link in x.find_all('a'):
              
               y=link.get('href')

               #SITE FOR ENGLISH SONG

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
                      print("   #########    ")
                      for p in soup.find_all("p",{"class":"verse"}):  
                         print("\n")
                         print(p.getText())

               #SITE FOR PUNJABI SONG    

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

                #SITE FOR PUNJABI SONG 
 
               if re.search(r'http://www.lyricsted.com/',y):
                  flag=1
                  s = y
                  start = s.find('q=')+2
                  end = s.find('&sa', start)
                  url_extract = s[start:end]
                  print(url_extract)

                  response = requests.get(url_extract)
                  
                  data = response.text
                  
                  soup = BeautifulSoup(data,"html.parser")
                  
                  for div in soup.find_all('div',{"class":"entry-content group"}): 
                    
                      for p in div.find_all("p"):  
                          text=p.getText()
                          if not re.search(r'lyrics',text):
                             print("\n")
                             print(p.getText())  
                              
                
               if re.search(r'https://www.musixmatch.com',y):
                  flag=1
                  s = y
                  start = s.find('q=')+2
                  end = s.find('&sa', start)
                  url_extract = s[start:end]
                  print(url_extract )   
                  headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106    Safari/537.36'}
                  response = requests.get(url_extract,headers=headers)
                
                  data = response.text
                  soup = BeautifulSoup(data,"html.parser")
                 
                  for div in soup.find_all('div',{"class":"mxm-lyrics"}): 
                      print("inside\n")
                      
                      for p in div.find_all("p",{"class":"mxm-lyrics__content"}):  
                          text=p.getText()
                          if not re.search(r'lyrics',text):
                             print("\n")
                             print(p.getText())                                
               
