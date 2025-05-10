class BookmarkJobPage:

    def __init__(self, page):
        self.page = page
        self.url = "https://labsqajobs.qaharbor.com/account/saved-jobs/"

        self.view_jobs_details = '(//span[@class="jet-listing-dynamic-link__label"])[4]' # saved jobs details
        self.view_jobs1_details = '(//span[@class="jet-listing-dynamic-link__label"])[8]' # saved jobs details

    
    def is_at(self):
        return self.page.url.startswith(self.url)

    def view_job_details(self):
        self.page.click(self.view_jobs_details)
        self.page.click(self.view_jobs1_details)
        self.page.wait_for_load_state("networkidle")


    # Add this method to get the current URL
    def get_current_url(self):
        return self.page.url

