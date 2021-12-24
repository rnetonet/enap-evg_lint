import asyncio
from playwright.sync_api import sync_playwright

class Robot:
    def __init__(self, login_url, login, password):
        with sync_playwright() as playwright:
            self.browser = playwright.chromium.launch(headless=False)
            self.browser_context = self.browser.new_context()
            self.page = self.browser_context.new_page()
            
            self.login(login_url, login, password)
            self.take_screenshot()

    def login(self, login_url, login, password):
        self.page.goto(login_url)
            
        self.page.fill("#usrCpfEmail", login)
        self.page.click("button")

        self.page.fill("#password", password)
        self.page.click("button")


    def take_screenshot(self):
        self.page.screenshot(path="screenshot.png", full_page=True)