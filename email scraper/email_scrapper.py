# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 11:52:07 2020

@author: Sharjeel Ahmed

Regex  for beautiful soup
"""

'''
Web Scraping - URLs and Email IDs
'''
# importing required libraries
import urllib.request 
from bs4 import BeautifulSoup

# URL TO SCRAP
wiki = "https://dlca.logcluster.org/display/public/DLCA/4.1+Nepal+Government+Contact+List"

#Query the website and return the html to the variable 'page'
#For python 3 use urllib.request.urlopen(wiki)
page = urllib.request.urlopen(wiki) 

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page,features='html.parser')
print('\n\nPage Scrapped !!!\n\n')

print('\n\nTITLE OF THE PAGE\n\n')
print(soup.title.string)


print('\n\nALL THE URLs IN THE WEB PAGE\n\n')


all_links = soup.find_all('a')


print('Total number of URLs present = ',len(all_links)) 


print('\n\nLast 5 URLs in the page are : \n')


if len(all_links) > 5 :
  
  last_5 = all_links[len(all_links)-5:]
  for url in last_5 :
    print(url.get('href'))


emails = []
for url in all_links :
    if(str(url.get('href')).find('@') > 0):
        emails.append(url.get('href'))


print('\n\nTotal Number of Email IDs Present: ', len(emails))

i=0
print('\n\nSome of the emails are: \n\n')
for email in emails[:]:
    i=i+1
    print(email,i)
    
