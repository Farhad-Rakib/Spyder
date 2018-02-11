
from bs4  import BeautifulSoup      #import BeautifulSoup package
import requests                     #import requests 
import io     
import mysql.connector
import _mysql     
from datetime import date, datetime, timedelta                 #import io for file read write

connection = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='spyder')

created_at = datetime.now().date()
updated_at = datetime.now().date()
scrapped_from = "BPSC"
#url from where data will be scrapped
scrapped_url = "http://www.bpsc.gov.bd/site/view/psc_exam/Non-Cadre%20Examination/%E0%A6%A8%E0%A6%A8-%E0%A6%95%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%A1%E0%A6%BE%E0%A6%B0-%E0%A6%AA%E0%A6%B0%E0%A7%80%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A6%BE"
#get html 
page = requests.get(scrapped_url) 
#using BeautifulSoup parsing the Html
scrapped_page = BeautifulSoup(page.text,'html.parser')
total_row = 0
for tr in scrapped_page.find_all('tr')[1:]:
    total_row +=1
    tds = tr.find_all('td')
    data= (scrapped_from,total_row,tds[1].text,tds[2].find('a').get('href'),"",created_at,updated_at)
    add_sql = ("INSERT INTO scrapped_data "
                "(scrapped_from, total_row_scrapped, scrapped_data_title, scrapped_data_url, scrapped_data_body,created_at,updated_at) "
                "VALUES (%s, %s, %s, %s, %s,%s,%s)")
    cursor = connection.cursor()
    cursor.execute(add_sql, data)
    connection.commit()
    cursor.close()
connection.close()