import re
from playwright.sync_api import Playwright, Page, expect
import time
import os

def test_main(playwright: Playwright):

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.apsema.com/ema/index.action")
    page.get_by_placeholder("Login Account").click()
    page.get_by_placeholder("Login Account").click()
    page.get_by_placeholder("Login Account").click()
    page.get_by_placeholder("Login Account").fill(os.environ['APSYSTEMS_USER'])
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(os.environ['APSYSTEMS_PWD'])
    page.get_by_role("button", name="Login").click()

    # Go to the page
    page.goto("https://www.apsema.com/ema/security/optmainmenu/intoLargeDashboard.action?language=en_US")

    time.sleep(3)
    
    element_today = page.locator("#today")    
    if element_today.inner_text() == "0":
        expect(page).to_have_title(re.compile("FAILED"))
    
    # ---------------------
    context.close()
    browser.close()
