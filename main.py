from selenium import webdriver
import time

chrome_driver_path = "C:\Development\chromedriver.exe"

class InternetSpeedBot:

    def __init__(self):
        self.up = 0
        self.down = 0
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_btn = self.driver.find_element_by_class_name("js-start-test")
        go_btn.click()
        time.sleep(20)
        internet_provider = self.driver.find_element_by_class_name("result-label")
        print(internet_provider.text)
        time.sleep(40)
        download_speed = self.driver.find_element_by_class_name("download-speed").text
        upload_speed = self.driver.find_element_by_class_name("upload-speed").text
        print(download_speed, upload_speed)
        if download_speed and upload_speed:
            self.tweet_at_internet_provider(download_speed, upload_speed)

    def tweet_at_internet_provider(self, down_speed=0, up_speed=0):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)
        input_field = self.driver.find_element_by_name("text")
        user_input = input("Please Enter username:")
        input_field.send_keys(user_input)
        next_btn = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]')
        next_btn.click()
        time.sleep(5)
        pwd_feild = self.driver.find_element_by_name("password")
        pwd = input("Please Enter Password:")
        pwd_feild.send_keys(pwd)
        login_btn = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div')
        login_btn.click()
        tweet_editor = self.driver.find_element_by_class_name("DraftEditor-root")
        tweet_editor.send_keys("Hi Internet Provider, Your Internet Speed is not what it was Promised.")
        time.sleep(2)
        tweet_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]')
        tweet_btn.click()



bot = InternetSpeedBot()
time.sleep(2)
bot.get_internet_speed()