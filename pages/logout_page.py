class LogoutPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://labsqajobs.qaharbor.com/"

    def is_at(self):
        return self.page.url.startswith(self.url)

    # Add this method to get the current URL
    def get_current_url(self):
        return self.page.url

