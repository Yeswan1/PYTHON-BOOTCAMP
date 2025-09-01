import threading
import requests
from bs4 import BeautifulSoup

urls=[
    'https://python.langchain.com/docs/introduction/',
    'https://python.langchain.com/docs/concepts/'
    

]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f"Fetched {len(soup.text)}characters from {url}")

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for threaf in threads:
    threaf.join()

print("fetched")