class SocialPages:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.linkedin.com/company/qa-harbor"
        self.url1 = "https://www.facebook.com/QAHarbor/"

    def navigate(self):
        self.page.goto(self.url)
        self.page.wait_for_load_state("networkidle")

    def navigate1(self):
        self.page.goto(self.url1)
        self.page.wait_for_load_state("networkidle")

        
    def get_current_url(self):
        return self.page.url