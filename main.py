from selenium import webdriver

chrome_driver_path = "C:\Users\pkabh\Downloads\ChromeSetup.exe"

class InternetSpeedBot:

    def __str__(self):
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        pass

    def tweet_at_internet_provider(self):
        pass

driver = webdriver.Chrome(executable_path=chrome_driver_path)


