class FindjobsPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://labsqajobs.qaharbor.com/find-jobs/"
        self.search_field = '(//input[@class="jet-search-filter__input"])[1]'
        #self.select_location = "//input[@id='confirm_password']" jet-select__control
        self.search_btn = '(//button[@class="apply-filters__button"])[1]' # search button

        self.Search_top_view_jobs = '(//span[@class="jet-listing-dynamic-link__label"])[4]' # search top view jobs
        self.apply_top_view_jobs = '//div[@class="elementor-widget-container"]/h2[text()="Apply Now"]' # apply top viewd jobs
        self.final_apply_top_view_jobs = '(//button[@class="jet-form-builder__action-button jet-form-builder__submit submit-type-ajax"])' # applied top viewd jobss
        self.top_view_jobs = '(//span[@class="jet-listing-dynamic-link__label"])[3]'
        self.top_view_jobs1 = '(//span[@class="jet-listing-dynamic-link__label"])[7]'
        #self.top_view_jobs3 = '(//span[@class="jet-listing-dynamic-link__label"])[11]'
        self.my_account = '(//span[@class="jet-auth-links__item-text"])[1]'    # go to my account page

    def is_at(self):
        return self.page.url.startswith(self.url)
    

    def bookmark_jobs(self):
        self.page.click(self.top_view_jobs)
        self.page.click(self.top_view_jobs1)
        self.page.wait_for_load_state("networkidle")

    def fill_search_jobs(self, search):
        self.page.fill(self.search_field, search)
        self.page.click(self.search_btn)
        self.page.wait_for_load_state("networkidle")

    def search_jobs(self):
        self.page.click(self.search_btn)
        self.page.wait_for_load_state("networkidle")

    def details_jobs_searched(self):
        self.page.click(self.Search_top_view_jobs)
        self.page.wait_for_load_state("networkidle")
    
    def apply_searched_jobs(self):
        self.page.click(self.apply_top_view_jobs)
        self.page.click(self.final_apply_top_view_jobs)
        self.page.wait_for_load_state("networkidle")
    
    def goto_myaccount(self):
        self.page.click(self.my_account)
        self.page.wait_for_load_state("networkidle")


    # Add this method to get the current URL
    def get_current_url(self):
        return self.page.url

