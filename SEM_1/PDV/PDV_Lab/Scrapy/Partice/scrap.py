from bs4 import BeautifulSoup
import requests

with open('home.html','r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content,'lxml')
    course = soup.find_all('div', class_='card')
    print(course[0].h5.text)
    print(course[0].a.text)


import pandas as pd

data = { 'name' = ["Ni","s",'G'],
        'ahe' = [23,23,23]
        }

df = pd.DataFrame(data,index=['a','b','c'])

print(df)

print(df.loc['b',['nmae','age']])
print(df.iloc[2,[0,1]])
import numpy as np

arr = np.array([[1,2,3],[1,2,3],[1,2,3]])
del_3 = np.delete(arr,2,axis = 1)
arr1 = np.array([[3,3,3]])
arr = np.inser(del_3,2,arr1,axis = 1)