class ChnagePasswordPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://labsqajobs.qaharbor.com/account/change-password/"
        self.own_email_summary = "//summary[contains(text(), 'view your account email address')]"
        self.new_password_field = "//input[@id='new_password']"
        self.new_confirm_password_field = "//input[@id='confirm_password']"
        self.submit_btn = "button[type='submit']"

    def is_at(self):
        return self.page.url.startswith(self.url)

    
    def fill_form(self, password, confirm_password):
        self.page.fill(self.new_password_field, password)
        self.page.fill(self.new_confirm_password_field , confirm_password)


    def change_password_submit(self):
        with self.page.expect_navigation():
            self.page.click(self.submit_btn)

    # Add this method to get the current URL
    def get_current_url(self):
        return self.page.url

