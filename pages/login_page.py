"""class LoginPage():
    def __init__(self, page):
        self.page = page
        self.username_input = "#email"
        self.password_input = "#password"
        self.signin_button = "button[type='submit']"

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.signin_button) 

# muple line comment in python?"""

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://labsqajobs.qaharbor.com/login/"
        self.email_field = "#email"
        self.password_field = "#password"
        self.submit_button = 'button[type="submit"]'
        self.error_message = ".error-message"
        self.create_account_btn = '(//span[@class="elementor-button-text"])[2]'

    def is_at(self):
        return self.page.url == self.url

    def enter_credentials(self, email, password):
        self.page.fill(self.email_field, email)
        self.page.fill(self.password_field, password)

    def submit(self):
        try:
            # Correct expected navigation URL
            with self.page.expect_navigation(url="https://labsqajobs.qaharbor.com/account/*"):
                self.page.click(self.submit_button)
            self.page.wait_for_load_state("networkidle")
        except Exception as e:
            if self.page.is_visible(self.error_message):
                error_text = self.page.inner_text(self.error_message)
                raise Exception(f"Login failed: {error_text}")
            raise e

    def go_to_registration(self):
        with self.page.expect_navigation():
            self.page.click(self.create_account_btn)
        self.page.wait_for_load_state("networkidle")
    
