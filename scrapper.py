from typing import final
from urllib import request
from attr import attrs
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
headers=["V_Mag(mv)","proper_name","bayer_designation","Distance(ly)","Spectral_class","hyperlink","Mass(M)","Radius(R)","Luminosity(L)"]
starsdata=[]
brightest_star_data=[]

def scrape():
    for i in range(0,428):

        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","stars"}):
            th_tags=ul_tag.find_all("th")
            temp_list=[]
            for index,th_tag in enumerate(th_tags):
                if index==0:
                    temp_list.append(th_tag.find_all("a")[0].contents[0])
                else:
                    try:

                        temp_list.append(th_tag.contents[0])
                    except:
                        temp_list.append("")
            hyperlink_li_tag=li_tags[0]
            temp_list.append("https://en.wikipedia.org/wiki/List_of_brown_dwarfs"+hyperlink_th_tag.find_all("a",href=True)[0]["href"])
            planetdata.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()


        def scrape_more_data(hyperlink):
        try:
        page=requests.get(hyperlink)
        soup=BeautifulSoup(page.content,"html.parser")
        for tr_tag in soup.find_all("tr",attrs={"class":"fact_rope"}):
            tr_tags=tr_tag.find_all("tr")
            temp_list=[]
            for tr_tag in tr_tags:
                try:
                    temp_list.append(tr_tag.find_all("div",attrs={"class":"value"})[0].contents[0])
                except:
                    temp_list.append("")
            brown_dwarf_data.append(temp_list)
    except:
        time.sleep(1)
        scrape_more_data(hyperlink)
scrape()
for data in starsdata:
    scrape_more_data(data[5])
final_stars_data=[]
for index,data in enumerate(starsdata):
    final_stars_data.append(data+final_stars_data[index])


with open("scraper.csv","w")as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(final_stars_data)