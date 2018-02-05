
from bs4  import BeautifulSoup      #import BeautifulSoup package
import requests                     #import requests 
import io                           #import io for file read write

#url from where data will be scrapped
scrapped_url = "http://www.bpsc.gov.bd/site/view/psc_exam/Non-Cadre%20Examination/%E0%A6%A8%E0%A6%A8-%E0%A6%95%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%A1%E0%A6%BE%E0%A6%B0-%E0%A6%AA%E0%A6%B0%E0%A7%80%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A6%BE"
#get html 
page = requests.get(scrapped_url) 
#using BeautifulSoup parsing the Html
scrapped_page = BeautifulSoup(page.text,'html.parser')

#file operation(write the parsed data into text file)
with io.open('D:\log.txt', 'a', encoding='utf8') as logfile:
    for tr in scrapped_page.find_all('tr')[1:]:
        tds = tr.find_all('td')
        logfile.write(u"%s, %s, %s\n" % (tds[0].text, tds[1].text, tds[2].find('a').get('href')))
