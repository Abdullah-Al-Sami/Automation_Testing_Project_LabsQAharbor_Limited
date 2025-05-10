from pathlib import Path

class UpdateProfilePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://labsqajobs.qaharbor.com/account/update-profile/"
        self.file_input_pic = '(//input[@name="_candidate_avatar"])[1]' 
        self.file_input_cv = '(//input[@class="jet-form-builder__field file-field jet-form-builder-file-upload__input"])[2]' 
        self.upload_success_pic = ".upload-success-pic"
        self.upload_success_cv = ".upload-success-cv"
        self.first_name = '(//input[@id="_candidate-first-name"])[1]'
        self.last_name = '(//input[@id="_candidate-last-name"])[1]'
        self.mobile_number = '(//input[@id="phone"])[1]'
        self.experience_year = '(//input[@id="_candidate-experience"])[1]'
        self.portfolio_link = '(//input[@class="jet-form-builder__field text-field"])[5]'
        self.listen_about_qaharbor = '(//input[@class="jet-form-builder__field text-field"])[6]'
        #self.agreement_radio = "//input[@name='_candidate-agreement' and @value='1']"
        self.yes_radio_label = "span:has-text('Yes')"
        self.file_input_cv = '(//input[@name="_candidate-resume"])[1]' 
        self.submit_button = '(//button[@class="jet-form-builder__action-button jet-form-builder__submit submit-type-ajax"])[1]'
        self.success_message = ".success-notice"
        self.error_message = ".error-notice"


    def is_at(self):
        return self.page.url == self.url
    
    def upload_files(self, image_path, cv_path):
        # Upload both files
        self.page.set_input_files(self.file_input_pic, image_path)
        self.page.set_input_files(self.file_input_cv, cv_path)
        
        # Wait for both success indicators
        #self.page.wait_for_selector(f"{self.upload_success_pic} >> nth=0", timeout=20000)
        #self.page.wait_for_selector(f"{self.upload_success_cv} >> nth=1", timeout=20000)
    

    def enter_credentials(self,firstname, lastname, mobile, portfolio, listenqa):
        self.page.fill(self.first_name, firstname)
        self.page.fill(self.last_name, lastname)
        self.page.fill(self.mobile_number, mobile)
        #self.page.fill(self.experience_year, experienceyear)
        self.page.fill(self.portfolio_link, portfolio)
        self.page.fill(self.listen_about_qaharbor, listenqa)
    
    def enter_experience(self):
        # Wait for field to be ready
        self.page.wait_for_selector(self.experience_year, state="visible")

        # Clear existing value and input 0.1
        self.page.fill(self.experience_year, "0.1")
        
        # Verify the input was successful
        actual_value = self.page.input_value(self.experience_year)
        
        if actual_value != "0.1":
            raise ValueError(f"Experience value not set correctly. Actual: {actual_value}")
    
    def select_yes(self):
    # Click the visible "Yes" text label
        self.page.click(self.yes_radio_label)
    # Verify selection
        radio_input = self.page.locator('input[name="_candidate-agreement"]')
        if not radio_input.is_checked():
            raise Exception("Radio button not selected after click")
    

    """def submit(self):
        try:
            # Correct expected navigation URL
            with self.page.expect_navigation(url="https://labsqajobs.qaharbor.com/account/update-profile/"):
                self.page.click(self.submit_button)
            self.page.wait_for_load_state("networkidle")
        except Exception as e:
            if self.page.is_visible(self.error_message):
                error_text = self.page.inner_text(self.error_message)
                raise Exception(f"Login failed: {error_text}")
            raise e"""

    def submit_profile_updatation(self):
        with self.page.expect_navigation():
            self.page.click(self.submit_button)
    
    