class SingleFindjobsPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://labsqajobs.qaharbor.com/find-jobs/"

        self.Search_top_view_jobs = '(//span[@class="jet-listing-dynamic-link__label"])[4]' # search top view jobs
        self.top_view_jobs = '(//span[@class="jet-listing-dynamic-link__label"])[3]'
        self.my_account = '(//span[@class="jet-auth-links__item-text"])[1]'    # go to my account page

    def is_at(self):
        return self.page.url.startswith(self.url)
    

    def bookmark_jobs(self):
        self.page.click(self.top_view_jobs)
        self.page.wait_for_load_state("networkidle")


    def details_jobs_searched(self):
        self.page.click(self.Search_top_view_jobs)
        self.page.wait_for_load_state("networkidle")
    
    def goto_myaccount(self):
        self.page.click(self.my_account)
        self.page.wait_for_load_state("networkidle")


    # Add this method to get the current URL
    def get_current_url(self):
        return self.page.url

