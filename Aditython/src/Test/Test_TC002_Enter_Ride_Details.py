__author__ = 'Aditya Roy'

import unittest
from time import sleep
from src.Main.BaseClass.EnvironmentSetup import EnvironmentSetup
from src.Utility.ExcelReader import *

class TC002_Enter_Ride_Details(EnvironmentSetup):
    def test_login(self):
        self.driver.get("http://100daysofcycling.com/my-account/")
        path = 'C:/Users/Laptop/PycharmProjects/Aditython/TestData/RideData.xlsx'
        data = getData(path,"RideData")

        self.driver.find_element_by_xpath("//input[@type='text' and @id='username']").send_keys("aditya.kgec91@gmail.com")
        self.driver.find_element_by_xpath("//input[@type='password'and @id='password']").send_keys("Russia@411")
        self.driver.find_element_by_xpath("//input[@type='submit' and @name='login']").click()

        sleep(3)
        self.driver.get("http://100daysofcycling.com/submit-data/")

        for i in data.index:
        #fetching data from excel and storing it to variable
            name = str(data["FirstName"][i])
            date = str(data["Date"][i])
            email = str(data["Email"][i])
            distance = str(data["Distance"][i])
            days = str(data["DaysReported"][i])
            print('Filling days for :'+days)

            self.driver.find_element_by_xpath("//*[@id='pdb-first_name']").send_keys(name)
            self.driver.find_element_by_xpath("//*[@id='pdb-country']").send_keys(date)
            self.driver.find_element_by_xpath("//*[@id='pdb-email']").send_keys(email)
            self.driver.find_element_by_xpath("//*[@id='pdb-distance_in_km']").send_keys(distance)
            self.driver.find_element_by_xpath(("//*[@id='pdb-days_reported_out_of_100']")).send_keys(days)
            self.driver.find_element_by_xpath("//input[@type='submit' and @name='submit_button']").click()

            updateResult(path, "RideData", "Result", "Updated Successfully", i,'Green')
            sleep(6)
            self.driver.execute_script("history.go(0)")

if __name__ == '__main__':
    unittest.main()




