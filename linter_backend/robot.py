from playwright.sync_api import sync_playwright

class Check:
    def __init__(self, description, result):
        self.description = description
        self.result = result
    
    def __str__(self) -> str:
        return f"{self.description}: {self.result}"

class Robot:
    def __init__(self, login_url, login, password, course_url):
        self.checks = []

        with sync_playwright() as playwright:
            self.browser = playwright.chromium.launch(headless=False)
            self.browser_context = self.browser.new_context()
            self.page = self.browser_context.new_page()
            
            self.login(login_url, login, password)
            self.take_screenshot()

    def login(self, login_url, login, password):
        try:
            self.page.goto(login_url)
                
            self.page.fill("#usrCpfEmail", login)
            self.page.click("button")

            self.page.fill("#password", password)
            self.page.click("button")

            self.checks.append(Check("Login", True))
            return True
        except:
            pass
        
        self.checks.append(Check("Login", False))
        return False

    def take_screenshot(self):
        self.page.screenshot(path="screenshot.png", full_page=True)