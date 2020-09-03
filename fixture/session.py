import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.app.open_home_page()
        self.app.driver.find_element(By.ID, "gb_70").click()
        self.app.driver.find_element(By.ID, "identifierId").send_keys(username)
        self.app.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-RLmnJb").click()
        time.sleep(3)
        self.app.driver.find_element(By.NAME, "password").click()
        self.app.driver.find_element(By.NAME, "password").send_keys(password)
        self.app.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-RLmnJb").click()
        time.sleep(2)

    def logout(self):
        self.app.driver.find_element(By.CSS_SELECTOR, ".gb_La").click()
        self.app.driver.find_element(By.ID, "gb_71").click()
        time.sleep(2)
        self.app.driver.find_element(By.CSS_SELECTOR, ".JDAKTe:nth-child(3) .BHzsHc").click()
        self.app.driver.find_element(By.CSS_SELECTOR, ".n3x5Fb path").click()
        time.sleep(2)
        element = self.app.driver.find_element(By.CSS_SELECTOR, ".M9Bg4d .RveJvd")
        actions = ActionChains(self.app.driver)
        actions.move_to_element(element).perform()
