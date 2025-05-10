class Subscribe:
    def __init__(self, page):
        self.page = page
        self.url = "https://labsqajobs.qaharbor.com/"
        self.email_field = "input[placeholder='Enter your email']"
        self.submit_btn = "button[type='submit']"

    def navigate(self):
        self.page.goto(self.url)
        self.page.wait_for_load_state("networkidle")

    def fill_form(self, email):
        self.page.fill(self.email_field, email)
    

    def submit_subcription(self):
        self.page.click(self.submit_btn)
        
    def get_current_url(self):
        return self.page.url