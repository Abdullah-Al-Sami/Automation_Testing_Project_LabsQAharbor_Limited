class CandidateRegistrationPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://labsqajobs.qaharbor.com/candidate-registration/"
        self.username_field = "//input[@id='username']"
        self.email_field = "//input[@id='email']"
        self.password_field = "//input[@id='password']"
        self.confirm_password_field = "//input[@id='conf-pass']"
        self.submit_btn = "button[type='submit']"

    def is_at(self):
        return self.page.url == self.url

    def fill_form(self, username, email, password, confirm_password):
        self.page.fill(self.username_field, username)
        self.page.fill(self.email_field, email)
        self.page.fill(self.password_field, password)
        self.page.fill(self.confirm_password_field , confirm_password)


    def submit_registration(self):
        with self.page.expect_navigation():
            self.page.click(self.submit_btn)
