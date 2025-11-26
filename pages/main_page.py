from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

from conftest import browser


class Mainpage:

    def __init__(self, browser):
        self.browser = browser



    def open(self):
        self.browser.get('https://only.digital/en')
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.browser.implicitly_wait(5)

    def click_cookie(self):
        time.sleep(5)
        cookie = self.browser.find_element(By.XPATH, '//button[@class="buttons Button_root__GbzzH Button_regular__RLX5e Button_secondary__pFIlL Cookie_rootButton__38Z2N"]')
        cookie.click()

    def check_footer(self):
        footer = self.browser.find_element(By.XPATH, '//div[@class="Footer_grid__lfZ34"]')
        footer.is_displayed()

    def check_logo(self):
        logo = self.browser.find_element(By.CLASS_NAME, 'Footer_logo__2QEhf')
        assert logo.is_displayed()

    def check_startproject(self):
        startproject = self.browser.find_element(By.XPATH, '//button[@class="buttons Button_root__GbzzH Button_regular__RLX5e Button_primary__swzAa StartProjectButton_root__jB_Lv  Footer_button__RHd0Q"]')
        assert startproject.is_displayed()

    def check_policy(self):
        policy = self.browser.find_element(By.XPATH, '//a[@class="text2 Footer_privacy__NdtU9"]')
        assert policy.is_displayed()

    def check_description(self):
        description = self.browser.find_element(By.XPATH, '//p[@class="text2 Footer_text___ATim"]')
        assert description.is_displayed()

    def check_year(self):
        year = self.browser.find_element(By.XPATH, '//p[@class="h4 Footer_year__nyNCc"]')
        assert year.is_displayed()

    def check_text(self):
        text = self.browser.find_element(By.XPATH, '//div[@class="copyrightsBig FooterText_root___Rdpb "]')
        assert text.is_displayed()

    def check_phone(self):
        phone = self.browser.find_element(By.XPATH, '//a[@class="TextLink_link__8n_Xi TextLink_regular__MLL6a text1"][2]')
        assert phone.is_displayed()

    def check_telegram(self):
        telegram = self.browser.find_element(By.XPATH, '//a[@class="TextLink_link__8n_Xi TextLink_regular__MLL6a text1"][1]')
        assert telegram.is_displayed()

    def check_email(self):
        email = self.browser.find_element(By.XPATH, '//div[@class="Socials_socialsWrap__DPtp_ Footer_socials__C39yX"]/following::a[3]')
        assert email.is_displayed()

    def check_social(self):
        social = self.browser.find_element(By.XPATH, '//div[@class="Socials_socialsWrap__DPtp_ Footer_socials__C39yX"]')
        assert social.is_displayed()

    def check_pdf(self):
        pdf = self.browser.find_element(By.XPATH, '//div[@class="Documents_documents__Ly1Oa"]/following::button[11]')
        assert pdf.is_displayed()

    def check_pitch(self):
        pitch = self.browser.find_element(By.XPATH, '//div[@class="Documents_documents__Ly1Oa"]/following::button[12]')
        assert pitch.is_displayed()