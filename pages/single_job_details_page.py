class SingleJobDetailsPage:

    def __init__(self, page):
        self.page = page
        self.url = "https://labsqajobs.qaharbor.com/jobs-vacancies/sr-automation-engineer/"
        self.url1 = "https://labsqajobs.qaharbor.com/account/saved-jobs/"
        

    # Add this method to get the current URL
    def get_current_url(self):
        return self.page.url
    
    def show_bookmark_jobs(self):
        self.page.click(self.bookmarked_jobs_button)
        self.page.wait_for_load_state("networkidle")

    def get_current_url1(self):
        return self.page.url1
    
