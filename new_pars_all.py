from selenium import webdriver
from time import sleep
import urllib.request
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from lxml.html import fromstring
import re
 
def getPhone(url):
    wd = webdriver.Chrome("C:/Users/zotik/Desktop/lol/chromedriver_win32/chromedriver.exe")
    wd.set_window_size(1366,768)
    sleep(1)
    wd.get(url)
    
    for _ in range(20):
        try:
            wd.find_element_by_link_text("Показать номер").click()
            break
        except:
            sleep(2)
    sleep(2)        
    print(wd.find_element_by_xpath('//*[@title="Телефон продавца"]').text)
    pop = re.sub("\D","",(wd.find_element_by_xpath('//*[@title="Телефон продавца"]').text))
    url1 = "http://www.kody.su/check-tel?number="+pop+"#text"
    checkPhone(get_html(url1))
    wd.quit()


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html)
    body = soup.find('body')
    section = body.find('section')
    for article in section.find_all('article'):
       for div in article.find_all('div'):
          for a in div.find_all('a'):
            fullurl = 'https://m.avito.ru'+a.get('href')
            getPhone(fullurl)          


def checkPhone(html):
    check = BeautifulSoup(html)
    body = check.find('body')
    for div in body.find_all('div', { "class" : "wrap" }):
        for td in div.find_all('td'):
            for strong in td.find_all('strong'):
                print(strong)

                
def main():
    print('Write your URL')
    url = input()
    i = 1
    while i <= 5:
        puck = url + "?=" + str(i)
        parse(get_html(puck))
        i = i + 1
        puck = str(0)

if __name__ == '__main__':
    main()
