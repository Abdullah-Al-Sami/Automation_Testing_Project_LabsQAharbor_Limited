class HomePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://labsqajobs.qaharbor.com/"
        self.sign_in_link = '(//span[@class="jet-auth-links__item-text"])[1]'
        self.click_linkedin = "a[href='https://www.linkedin.com/company/qa-harbor']" # LinkedIn link
        self.click_facebook = "a[href='https://www.facebook.com/QAHarbor/']" # Facebook link

    def navigate(self):
        self.page.goto(self.url)
        self.page.wait_for_load_state("networkidle")

    def click_sign_in(self):
        self.page.click(self.sign_in_link)
        self.page.wait_for_load_state("networkidle")

    def click_linkdedin_page(self):
        self.page.click(self.click_linkedin)
        self.page.wait_for_load_state("networkidle")
    
    def click_facebook_page(self):
        self.page.click(self.click_facebook)
        self.page.wait_for_load_state("networkidle")

    # Add this method to get the current URL
    def get_current_url(self):
        return self.page.url