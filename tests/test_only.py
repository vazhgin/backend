from pages.main_page import Mainpage

def test_cookie(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    mainpage.click_cookie()

def test_footer(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    mainpage.check_footer()

def test_logo(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    mainpage.check_logo()

def test_startproject(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    mainpage.check_startproject()

def test_policy(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    mainpage.check_policy()

def test_description(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    mainpage.check_description()

def test_year(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    mainpage.check_year()

def test_text(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    mainpage.check_text()

def test_phone(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    mainpage.check_phone()

def test_telegram(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    mainpage.check_telegram()

def test_email(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    mainpage.check_email()

def test_social(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    mainpage.check_social()

def test_pdf(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    mainpage.check_pdf()

def test_pitch(browser):
    mainpage = Mainpage(browser)
    mainpage.open()
    mainpage.check_pitch()