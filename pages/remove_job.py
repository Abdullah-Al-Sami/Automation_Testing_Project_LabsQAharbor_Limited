class RemoveJobPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://labsqajobs.qaharbor.com/account/saved-jobs/"
        self.remove_bookmarked = '(//span[@class="jet-listing-dynamic-link__label"])[3]' # Removed saved jobs details

    # Add this method to get the current URL
    def get_current_url(self):
        return self.page.url
    
    def remove_bookmarked_job(self):
        self.page.click(self.remove_bookmarked)