import bs4 as bs

import urllib.request

req = urllib.request.Request('https://www.udemy.com/courses/search/?src=ukw&q=python',headers={'User-Agent':'Mozilla/5.0'})

resp=urllib.request.urlopen(req)

#print(resp.read())

soup = bs.BeautifulSoup(resp,'html')

#print(soup.title)

for link in soup.find_all('a'):
    print(link.string)