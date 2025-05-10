class JobDetailsPage:

    def __init__(self, page):
        self.page = page
        self.url = "https://labsqajobs.qaharbor.com/jobs-vacancies/sr-automation-engineer/"
        self.url1 = "https://labsqajobs.qaharbor.com/account/saved-jobs/"
        self.url2 = "https://labsqajobs.qaharbor.com/jobs-vacancies/senior-sqa-engineer-2/"
        self.url3 ="https://labsqajobs.qaharbor.com/account/applied/" # watch applied jobs
        

    # Add this method to get the current URL
    def get_current_url(self):
        return self.page.url
    
    def goto_bookmark_job(self):
        self.page.goto(self.url1)

    def get_current_url1(self):
        return self.page.url1
    
    def get_current_url2(self):
        return self.page.url2
    
    def get_current_url3(self):
        return self.page.url3