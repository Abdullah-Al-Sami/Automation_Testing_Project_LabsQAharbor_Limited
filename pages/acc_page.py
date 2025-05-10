class Acc_Page:
    def __init__(self, page):
        self.page = page
        self.url = "https://labsqajobs.qaharbor.com/account/"
        self.bookmarked_jobs_button = "a[href='https://labsqajobs.qaharbor.com/account/saved-jobs/']"

    def is_at(self):
        try:
            # Verify both URL and visible elements
            self.page.wait_for_url(self.url, timeout=15000)
            #self.page.wait_for_selector(self.dashboard_element, state="visible", timeout=15000)
            return True
        except:
            return False
        
    def show_bookmark_jobs(self):
        self.page.click(self.bookmarked_jobs_button)
        self.page.wait_for_load_state("networkidle")
        
    # Add this method to get the current URL
    def get_current_url(self):
        return self.page.url