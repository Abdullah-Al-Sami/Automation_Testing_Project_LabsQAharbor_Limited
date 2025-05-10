class RegistrationPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://labsqajobs.qaharbor.com/registration/"
        self.candidate_btn = '(//div[@class="jet-button__state jet-button__state-hover"])[3]'

    def is_at(self):
        return self.page.url.startswith(self.url)

    def select_candidate_role(self):
        # DOMContentLoaded
        with self.page.expect_navigation(wait_until="domcontentloaded"):
            self.page.click(self.candidate_btn)

