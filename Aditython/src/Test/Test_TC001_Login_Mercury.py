__author__ = 'Aditya Roy'

import unittest
from time import sleep
from src.Main.BaseClass.EnvironmentSetup import EnvironmentSetup
from src.Utility.ExcelReader import *

class TC001_login_mercury(EnvironmentSetup):

    def test_login(self):
        self.driver.get("http://newtours.demoaut.com/")
        path = 'C:/Users/Laptop/PycharmProjects/Aditython/TestData/TestData.xlsx'
        data = getData(path,"userData")

        for i in data.index:
        #fetching data from excel and storing it to variable
            userName = str(data["UserName"][i])
            password = str(data["Password"][i])
            print('Trying login with :' + str(data["UserName"][i]) + '/' + str(data["Password"][i]))

            self.driver.find_element_by_name("userName").send_keys(userName)
            self.driver.find_element_by_name("password").send_keys(password)
            self.driver.find_element_by_name("login").click()
            sleep(2)

            if self.driver.title == "Find a Flight: Mercury Tours:":
                print("Test Passed")
                updateResult(path,"userData","Result","Pass Successfully",i,'Green')
                updateExecutionCompletion(path,"userData",i)
            else:
                print("Test Failed")
                updateResult(path, "userData", "Result", "Test Failed",i,'Red')
                updateExecutionCompletion(path,"userData",i)

            #going back to home page
            self.driver.find_element_by_link_text("Home").click()


if __name__ == '__main__':
    unittest.main()