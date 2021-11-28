from bs4 import BeautifulSoup
import requests
import re
#The pages could be inserted from beginning to end and done with a loop without input
i = int(input('PAGE: '))
r = requests.get('https://www.digikala.com/treasure-hunt/products/?pageno=%s&sortby=4' %(i))
soup = BeautifulSoup(r.text , 'html.parser')
rest = soup.find_all('a' , attrs={'class' : 'c-product-box__img c-promotion-box__image js-url js-product-item js-product-url'})
res = []
for k in range(0,len(rest)):
    res = res + [str(rest[k])]
link = []
for j in range(0,len(res)):
    n1 = re.findall(r'href=.(.*)\" target',res[j])
    link = link + n1
l = 0
for q in range(0,len(link)):
    rr = requests.get('https://www.digikala.com%s' %link[q])
    soupss = BeautifulSoup(rr.text , 'html.parser')
    redt = soupss.find_all('img', attrs={'class' : 'pannable-image'})
    for ax in redt:
        links = ax['data-high-res-src']
        l = l + 1
        name = str(l)
        with open(name + '.jpg' , 'wb') as f :
           im = requests.get(links)
           f.write(im.content)