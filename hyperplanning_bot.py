from selenium import webdriver
from time import sleep
from datetime import *
from credentials import username, password
import pyscreenshot as ImageGrab

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

class edtBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        print("init ok")

    def login(self):
        print("login")
        self.driver.get('planning_URL')
        
        # full screen
        # self.driver.manage().window().maximize()

        sleep(3) #wait a bit for loading the page

        username_in = self.driver.find_element_by_xpath('//*[@id="id_62"]')
        username_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="id_63"]')
        pw_in.send_keys(password)

        sleep(3)

        login_btn = self.driver.find_element_by_xpath('//*[@id="id_51"]')
        login_btn.click()

        sleep(3)

        # view all the planning of the week
        show_edt_btn = self.driver.find_element_by_xpath(
            '//*[@id="GInterface.Instances[0].Instances[1]_Combo0"]')
        show_edt_btn.click()

        sleep(3)

    def takeScreenshot(self):
        screenshot = ImageGrab.grab()
        myDate = datetime.datetime.now()
        title = ""
        title += str(myDate.day)+"_"+str(myDate.month)+"_"+str(myDate.year)+"_"
        title += str(myDate.hour)+"_"+str(myDate.minute)+"_"+str(myDate.second)+".png"
        ImageGrab.grab_to_file(title)
        print ("Screenshot saved as "+title)

    def deconnect(self):
        deconnect_first_btn = self.driver.find_element_by_xpath(
            '//*[@id="GInterface.Instances[0].Instances[0]"]/div/div[2]/div/div[2]/div[4]')
        deconnect_first_btn.click()
        sleep(3)

        action = webdriver.common.action_chains.ActionChains(driver)
        base_window = self.driver.window_handles[0]
        # click on the confirmation pop-up
        action.move_to_element_with_offset(base_window, 447, 802) 
        action.click()
        action.perform()  # needed

def launchBot():
    print("launch ok")
    bot = edtBot()
    bot.login()
    bot.takeScreenshot()
    bot.deconnect()