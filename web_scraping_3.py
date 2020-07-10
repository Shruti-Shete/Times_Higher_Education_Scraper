from bs4 import BeautifulSoup
import requests
import csv



from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get(
    "https://www.timeshighereducation.com/world-university-rankings/2020/world-ranking#!/page/0/length/100/sort_by/rank/sort_order/asc/cols/stats")

res = driver.execute_script("return document.documentElement.outerHTML")


soup = BeautifulSoup(res, 'html.parser')
box = soup.find_all('table', id_= 'datatable-1')

row = len(driver.find_elements_by_xpath("//*[@id='datatable-1']/tbody/tr"))
col = len(driver.find_elements_by_xpath("//*[@id='datatable-1']/tbody/tr/td"))
print(row)
print(col)


for rows in range(1,row+1):
    for cols in range(1,3):
        f = driver.find_element_by_xpath("//*[@id='datatable-1']/tbody/tr["+str(rows)+"]/td["+str(cols)+"]").text
        print(f)


