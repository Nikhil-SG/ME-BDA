from bs4 import BeautifulSoup
import requests

url = 'hello.com'
html = requests.get(url)
soup = BeautifulSoup(html,'html.parser')
books = soup('a',"class_ = books").text
bat = soup.find_all('div',"class_ = bats")
for bats in bat:
    