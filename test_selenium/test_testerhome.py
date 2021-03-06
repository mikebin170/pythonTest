from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver.common.action_chains import ActionChains


#进入testerhome，访问MTSC2020置顶帖，点击目录，点击议题征集范围。把代码贴到回复里

class TestTestsele():

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        self.driver.maximize_window()
        self.vars = {}

    def wait(self, timeout, method):
        WebDriverWait(self.driver, timeout).until(method)

    def teardown_method(self, method):
        self.driver.quit()

    def test_page(self):
        element1 = (By.CSS_SELECTOR, '.topic:nth-child(2) [title="MTSC2020 中国互联网测试开发大会议题征集"]')
        # self.driver.find_element(By.LINK_TEXT, "MTSC2020 中国互联网测试开发大会议题征集").click()
        # self.driver.find_element(By.CSS_SELECTOR, '.topic:nth-child(2)[title="MTSC2020 中国互联网测试开发大会议题征集"]').click()
        self.wait(10, expected_conditions.element_to_be_clickable(element1))
        self.driver.find_element(*element1).click()

        element2 = (By.CSS_SELECTOR, '.toc-container:nth-child(1) button')
        self.wait(10, expected_conditions.element_to_be_clickable(element2))
        self.driver.find_element(*element2).click()

        # WebDriverWait(self.driver, 10).until(lambda x: self.driver.find_element(element2) > 1)
        #使用lambda表达式
        # WebDriverWait(self.driver, 10).until(lambda x: self.driver.find_element(By.CSS_SELECTOR, '.toc-container:nth-child(1) button')).click()

        element3 = (By.LINK_TEXT, '提交议题格式')
        self.wait(10, expected_conditions.element_to_be_clickable(element3))
        self.driver.find_element(*element3).click()
