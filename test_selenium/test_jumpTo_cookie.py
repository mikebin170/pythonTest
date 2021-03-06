# Author:xiaobin
# Time:2020/1/3 18:00
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


# 使用cookie跳过登陆
class TestWorkWX:

    # 每个测试用例执行前调用的方法，进行浏览器打开，页面打开等设定
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        # self.driver.get('https://testerhome.com')

        url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
        self.driver.get(url)
        cookies = {
            "wwrtx.vst": "2MRo_7ZsVG8p0HKhl7-I5h-Guis6glWrsbNWk-eYEIPjysa05GFPAsMztP_6GUxnuk2nk--PPGcE1tHMZh5eyfjMdV_lIHoAj3QT41kRUadL67tdn52eWWL4-L9l7PKFTDX0LS5CEC7IZtI6TbJjR6vYluJo6CzeAqf11oudjZzSElOO6qShAFFjQhY5MCc7s1i8EK_N6mp8SqAiSDb0-nrWLGdadlyqODM2WtC2isUi1Oh0ilN87y3k8ALzzy--wCaeFF-UKamFMiyH6JCkyQ",
            "wwrtx.d2st": "a1885006",
            "wwrtx.sid": "fVdwbDnUnCt31o0z5JR4JXSJ2ttIjOV0A-Iu4XQBijjlmGueg_TJeuySSuFRXqcC",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970325079096544",
            "wxpay.vid": "1688849993369363",
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.driver.get(url)

    # 每个测试用例执行完毕之后调用的方法，进行退出操作
    # def teardown_method(self):
    #     self.driver.quit()

    # 添加成员页面的填写成员信息
    def test_add_member(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, '#menu_contacts').click()
        self.driver.find_element(By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member').click()
        # time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys("testerhome001")  # 姓名
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_english_name').send_keys("test001")  # 别名
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys("test001")  # 座机帐号
        self.driver.find_element(By.CSS_SELECTOR, 'label:nth-child(2) input').click()  # 性别单选框
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_phone').send_keys("13688889999")  # 手机
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_telephone').send_keys("13688889999")  # 座机
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_mail').send_keys("13688889999@163.com")  # 邮箱
        self.driver.find_element(By.CSS_SELECTOR, '#memberEdit_address').send_keys("00001员工地址")  # 地址
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_title').send_keys("架构师")  # 职务
        self.driver.find_element(By.XPATH, '//div/label[2]/input[@name="identity_stat"]').click()  # 身份
        self.driver.find_element(By.XPATH, '//div/label[2]/input[@name="extern_position_set"]').click()  # 对外职务-选择自定义
        self.driver.find_element(By.CSS_SELECTOR, '[name = "extern_position"]').send_keys("项目经理")  # 对外职务-自定义输入
        self.driver.find_element(By.CSS_SELECTOR, '[name="sendInvite"]').click()  # 通过邮件或短信发送企业邀请
        self.driver.find_element(By.CSS_SELECTOR, '.qui_btn.ww_btn.js_btn_save').click()
