class AccountPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://labsqajobs.qaharbor.com/account/"

        self.show_jobs_applied = "a[href='https://labsqajobs.qaharbor.com/account/applied/']"
        self.find_jobs_button = '(//div[@class="jet-button__state jet-button__state-hover"])[1]'
        self.bookmarked_jobs_button = "a[href='https://labsqajobs.qaharbor.com/account/saved-jobs/']"
        self.profile_completion_button = '(//span[@class="jet-button__icon jet-elements-icon"])[1]' #Edit your profile information button
        self.edit_profile_form = '(//span[@class="elementor-button-text"])[2]' #Edit your profile information page
        self.change_password_button = "a[href='https://labsqajobs.qaharbor.com/account/change-password/']"
        self.logout_button = '(//span[@class="jet-auth-links__item-text"])[2]'

    def is_at(self):
        try:
            # Verify both URL and visible elements
            self.page.wait_for_url(self.url, timeout=15000)
            #self.page.wait_for_selector(self.dashboard_element, state="visible", timeout=15000)
            return True
        except:
            return False
    
    def find_jobs(self):
        self.page.click(self.find_jobs_button)
        self.page.wait_for_load_state("networkidle")

    def edit_profile(self):
        self.page.click(self.profile_completion_button)
        self.page.wait_for_load_state("networkidle")

    def edit_profile_page(self):
        self.page.click(self.edit_profile_form)
        self.page.wait_for_load_state("networkidle")
    
    def show_bookmark_jobs(self):
        self.page.click(self.bookmarked_jobs_button)
        self.page.wait_for_load_state("networkidle")
        
    def change_password(self):
        self.page.click(self.change_password_button)
        self.page.wait_for_load_state("networkidle")
    
    def show_applied_jobs(self):
        self.page.click(self.show_jobs_applied)
        self.page.wait_for_load_state("networkidle")
    
    def log_out(self):
        self.page.click(self.logout_button)
        self.page.wait_for_load_state("networkidle")

    # Add this method to get the current URL
    def get_current_url(self):
        return self.page.url