from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pandas as pd
import re
import csv
from tabulate import tabulate
# options = webdriver.ChromeOptions()
# options.add_argument("incognito")
# options.add_argument("--headless")


# driver = webdriver.Chrome()
# driver.get("https://goodinfo.tw/tw/StockFinDetail.asp?RPT_CAT=IS_M_QUAR_ACC&STOCK_ID=2727")
# time.sleep(1)
# driver.execute_script("window.scrollBy(0, window.innerHeight)")
# time.sleep(3)
# select_element = driver.find_element(By.ID, 'RPT_CAT')
# select = Select(select_element)

# select.select_by_value("IS_M_YEAR")
# time.sleep(2)
# soup = BeautifulSoup(driver.page_source, "html.parser")
# driver.close()
# table_html=soup.find_all('table',id="tblFinDetail" ,class_='b1 p4_4 r0_10 row_mouse_over' )
# #table_html = table_html.prettify()
# #df = pd.read_html(table_html)
# #print(df)


# with open("2727_profit_table.txt", "w", encoding="utf-8") as file:
#     file.write(str(table_html))
with open("2727_profit_table.txt", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")
    table_html = soup.prettify()
df = pd.read_html(table_html)
print(df)

df[0].to_csv("2727_profit_table.csv",encoding="utf-8-sig",index=False)

data = pd.read_csv('2727_profit_table.csv')
