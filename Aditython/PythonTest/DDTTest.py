__author__ = 'Aditya Roy'

from selenium import webdriver
from ddt import ddt, data,unpack
import unittest
import xlrd
import nose
import datetime

def getData(fileName):
    book = xlrd.open_workbook(fileName)
    sheet = book.sheet_by_index(0)
    record = []
    for row_index in range(1,sheet.nrows):
        record.append(list(sheet.row_values(row_index, 0, sheet.ncols)))
    return record

@ddt
class DDTTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome("D:\BrowserDriver\ChromeDriver\chromedriver.exe")
        print("Run Started at :" + str(datetime.datetime.now()))
        print("Chrome Environment Set Up")
        print("------------------------------------------------------------------")
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    @data(*getData("C:/Users/Laptop/Desktop/TestData.xlsx"))
    @unpack
    def test_SearchResults(self, values):
        self.driver.get("https://www.google.com/")
        self.search_field = self.driver.find_elements_by_xpath("//*[@id='lst-ib'][@title='Search']")
        self.search_field.clear()
        self.search_field.send_keys(values)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()