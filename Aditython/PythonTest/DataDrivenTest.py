__author__ = 'Aditya Roy'

import ExcelReader
from selenium import webdriver
from pandas import *
from time import sleep

driver = webdriver.Chrome("D:\BrowserDriver\ChromeDriver\Version70-72\chromedriver.exe")

driver.maximize_window()

path = "E:\TestData.xlsx"
# rows = ExcelReader.r_count(path,"sheet1")
#
# for r in range (2,rows+1):
#     userName = ExcelReader.readData(path,"sheet1",r,1)
#     password = ExcelReader.readData(path,"sheet1",r,2)
#
#     driver.find_element_by_name("userName").send_keys(userName)
#     driver.find_element_by_name("password").send_keys(password)
#     driver.find_element_by_name("login").click()
#
#     if driver.title == "Find a Flight: Mercury Tours:":
#         print("Test Passed")
#         ExcelReader.writeData(path,"sheet1",r,3,"Passed")
#     else:
#         print("Test Failed")
#         ExcelReader.writeData(path,"sheet1",r,3,"Failed")
#     driver.find_element_by_link_text("Home").click()

df = read_excel(path, sheet_name="sheet1")
for i in df.index:
    print ("Trying login with :"+df["UserName"][i]+"/"+df["Password"][i])
    driver.find_element_by_name("userName").send_keys(df["UserName"][i])
    driver.find_element_by_name("password").send_keys(df["Password"][i])
    driver.find_element_by_name("login").click()
    sleep(2)
    driver.find_element_by_link_text("Home").click()

