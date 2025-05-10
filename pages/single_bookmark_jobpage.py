class SingleBookmarkJobPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://labsqajobs.qaharbor.com/account/saved-jobs/"

        self.view_jobs = '(//span[@class="jet-listing-dynamic-link__label"])[4]' # saved jobs details

    
    def is_at(self):
        return self.page.url.startswith(self.url)

    def view_job_details(self):
        self.page.click(self.view_jobs)
        self.page.wait_for_load_state("networkidle")


    # Add this method to get the current URL
    def get_current_url(self):
        return self.page.url

