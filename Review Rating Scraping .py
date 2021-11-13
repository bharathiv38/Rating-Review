#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing Libraries
import selenium
import pandas as pd
import time
from bs4 import BeautifulSoup

#import selenium webdriver
from selenium import webdriver

#import required exceptions which needs to handled
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

#import request
import requests

#import regrex
import re


# # Scraping data from Flipkart

# In[2]:


#listing out url for calling function
function =[]
for i in range(1,501):
    c_f=(f"https://www.flipkart.com/jackly-square-precision-32-pc-ratchet-screwdriver-set/product-reviews/itmee8fwhfecezhz?pid=SCSEE8FWZQMBQKQU&lid=LSTSCSEE8FWZQMBQKQU0FINF6&marketplace=FLIPKART&page={i}")
    function.append(c_f)


# In[3]:


#function defination
review = []
rating =[]
def tool_kit(url):
    driver=webdriver.Chrome(r"C:\Users\Laptop\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get(url)
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    for i in soup.find_all("div",class_='t-ZTKy'):
        review.append(i.text)
    for i in soup.find_all("div",class_=["_3LWZlK _1BLPMq","_3LWZlK _32lA32 _1BLPMq","_3LWZlK _1rdVr6 _1BLPMq"]):
        rating.append(i.text)
        
#callingout the function
for i in function:
    tool_kit(i)


# In[4]:


len(rating)


# In[5]:


len(review)


# In[6]:


df=pd.DataFrame({"Reveiw":review,
                "Rating":rating})
print(df.head)
df.to_csv('RR1',index=False)


# # Scraping review rating for adjustable dumbell

# In[8]:


#listing out url for calling function
function=[]
for i in range(1,116):
    c_f=(f"https://www.flipkart.com/pro-toner-pvc-16kg-star-nut-rod-adjustable-dumbbell/product-reviews/itmf3vd9nuwvx8xf?pid=DBLESEHG22MVXYHZ&lid=LSTDBLESEHG22MVXYHZXMWUHQ&marketplace=FLIPKART&page={i}")
    function.append(c_f)


# In[9]:


#function definition
review2=[]
rating2=[]
def tool_kit(url):
    driver=webdriver.Chrome(r"C:\Users\Laptop\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get(url)
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    for i in soup.find_all("div",class_='t-ZTKy'):
        review2.append(i.text)
    for i in soup.find_all("div",class_=["_3LWZlK _1BLPMq","_3LWZlK _32lA32 _1BLPMq","_3LWZlK _1rdVr6 _1BLPMq"]):
        rating2.append(i.text)
        
#calling function
for i in function:
    tool_kit(i)


# In[10]:


len(review2)


# In[11]:


len(review2)


# In[12]:


df=pd.DataFrame({})
df['Review']=review2
df["Rating"]=rating2
df


# In[13]:


df.to_csv('RR2', index = False)


# # Scraping data for Oppo phone

# In[14]:


#listing out url for calling function
function=[]
for i in range(1,301):
    c_f=(f"https://www.flipkart.com/oppo-a53s-5g-ink-black-128-gb/product-reviews/itm7dd84770173a5?pid=MOBG25PGGVWXR727&lid=LSTMOBG25PGGVWXR727NUADZM&marketplace=FLIPKART&page{i}")
    function.append(c_f)
         


# In[15]:


#function definition
review3=[]
rating3=[]
def hair_curler(url):
    driver=webdriver.Chrome(r"C:\Users\Laptop\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get(url)
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"html.parser")
    for i in soup.find_all("div",class_="t-ZTKy"):
        review3.append(i.text)
    for i in soup.find_all("div",class_=["_3LWZlK _1BLPMq","_3LWZlK _1BLPMq","_2-N8zT"]):
        rating3.append(i.text)
    
#calling fuction
for i in function:
    hair_curler(i)


# In[16]:


len(review3)


# In[17]:


len(rating3)


# In[18]:


df=pd.DataFrame({})
df['Review']=review3
df['Rating']=rating3
df


# In[19]:


df.to_csv('RR3', index=False)


# # Scraping Data for hair straightner from Amazon

# In[22]:


# Listing out url for calling Function
function=[]
for i in range(1,51):
    c_f=(f"https://www.amazon.in/Vega-VHSCC-01-Instant-Style-Styler/product-reviews/B071J3YJ73/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber={i}")
    function.append(c_f)


# In[23]:


# Function Definition
review_list=[]
def hair_s(url):
    driver=webdriver.Chrome(r"C:\Users\Laptop\Downloads\chromedriver_win32\chromedriver.exe")# Activating the chrome browser
    driver.get(url)
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    reviews=soup.find_all('div',{'data-hook' : 'review'})
    try:
        for item in reviews:
            review={    
            'Review' : item.find('span',{'data-hook':'review-body'}).text.strip(),
            'Rating': float(item.find('i',{'data-hook':'review-star-rating'}).text.replace('out of 5 stars',"").strip())
            }
            review_list.append(review)
    except:
        pass   
#calling function
for i in function:
    hair_s(i)


# In[26]:


review_list


# In[27]:


df = pd.DataFrame(review_list)
df.to_csv('RR4', index=False)
df


# # Scraping Laptop Data

# In[29]:


# Listing out url for calling Function
function=[]
for i in range(1,51):
    c_f=(f"https://www.amazon.in/Lenovo-IdeaPad-Warranty-Platinum-81WE01P5IN/product-reviews/B09G9YCHZ8/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber={i}")
    function.append(c_f)


# In[30]:


# Function Definition
review_list=[]
def laptop(url):
    driver=webdriver.Chrome(r"C:\Users\Laptop\Downloads\chromedriver_win32\chromedriver.exe")# Activating the chrome browser
    driver.get(url)
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    reviews=soup.find_all('div',{'data-hook' : 'review'})
    try:
        for item in reviews:
            review={    
            'Review' : item.find('span',{'data-hook':'review-body'}).text.strip(),
            'Rating': float(item.find('i',{'data-hook':'review-star-rating'}).text.replace('out of 5 stars',"").strip())
            }
            review_list.append(review)
    except:
        pass   
#calling function
for i in function:
    laptop(i)


# In[31]:


review_list


# In[32]:


df = pd.DataFrame(review_list)
df.to_csv('RR5', index=False)
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




