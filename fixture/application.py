from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
    def logout(self):
        self.driver.find_element(By.CSS_SELECTOR, ".gb_La").click()
        self.driver.find_element(By.ID, "gb_71").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".JDAKTe:nth-child(3) .BHzsHc").click()
        self.driver.find_element(By.CSS_SELECTOR, ".n3x5Fb path").click()
        time.sleep(2)
        element = self.driver.find_element(By.CSS_SELECTOR, ".M9Bg4d .RveJvd")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def send_email(self, group):
        element = self.driver.find_element(By.LINK_TEXT, "Gmail")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Gmail").click()
        self.driver.find_element(By.CSS_SELECTOR, ".T-I-KE").click()
        time.sleep(3)
        self.driver.find_element(By.NAME, "to").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "to").send_keys("ruratesting@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.NAME, "subjectbox").send_keys(group.title)
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[22]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Надіслані").click()
        time.sleep(2)


    def login(self, username, password):
        self.open_home_page()
        self.driver.find_element(By.ID, "gb_70").click()
        self.driver.find_element(By.ID, "identifierId").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-RLmnJb").click()
        time.sleep(3)
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-RLmnJb").click()
        time.sleep(2)

    def open_home_page(self):
        self.driver.get("https://www.google.com.ua/")

    def destroy(self):
        self.driver.quit()

