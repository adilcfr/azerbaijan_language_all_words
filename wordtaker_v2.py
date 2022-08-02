import requests as rq
from bs4 import BeautifulSoup
import time

start=time.time()
say=0
file = open('aze_all_words_2.txt','a', encoding='utf8')
url='https://obastan.com/azerbaycan-dilinin-orfoqrafiya-lugeti/a/?l=az&p='
pagesay=0
for i in range(1,2036):
    page = rq.get(url+str(i))
    html = page.text.encode('utf8')
    soup = BeautifulSoup(html, 'html.parser')
    soz = soup.find_all("h3")
    pagesay+=1
    for j in range(len(soz)):
        if(soz[j].string!=None):
            say+=1
            file.write(soz[j].string+'\n')
            #print(soz[j].string,say)
    print(pagesay)

file.close()

end=time.time()
print('vaxt')
print(end-start)
print('sozsayi')
print(say)

#print(soz[49].string)