from selenium.webdriver import ActionChains
import time

from selenium.webdriver.common.by import By


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def send_email(self, group):
        element = self.app.driver.find_element(By.LINK_TEXT, "Gmail")
        actions = ActionChains(self.app.driver)
        actions.move_to_element(element).perform()
        time.sleep(2)
        self.app.driver.find_element(By.LINK_TEXT, "Gmail").click()
        self.app.driver.find_element(By.CSS_SELECTOR, ".T-I-KE").click()
        time.sleep(3)
        self.app.driver.find_element(By.NAME, "to").click()
        time.sleep(2)
        self.app.driver.find_element(By.NAME, "to").send_keys("ruratesting@gmail.com")
        time.sleep(2)
        self.app.driver.find_element(By.NAME, "subjectbox").send_keys(group.title)
        time.sleep(2)
        self.app.driver.find_element(By.XPATH,
                                     "/html/body/div[22]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]").click()
        time.sleep(2)
        self.app.driver.find_element(By.LINK_TEXT, "Надіслані").click()
        time.sleep(2)
