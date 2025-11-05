from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, username: str, password: str):
        self.page.fill("input[placeholder='Username']", username)
        self.page.fill("input[placeholder='Password']", password)
        self.page.click("button[type='submit']")

    def logo(self):
            return self.page.locator("//img[@alt='client brand banner']")
  
