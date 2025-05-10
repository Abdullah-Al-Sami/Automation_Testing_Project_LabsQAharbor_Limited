from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.candidate_registration_page import CandidateRegistrationPage

#Valid account creation 1 (Already Not Created Account)
def test_account_creation(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    reg_page = RegistrationPage(page)
    candidate_reg_page = CandidateRegistrationPage(page)

    # Step 1: Navigate to home page
    home_page.navigate()

    # Step 2: Go to login page
    home_page.click_sign_in()
    assert login_page.is_at(), "Not on login page"

    # Step 3: Navigate to registration page
    login_page.go_to_registration()
    print("Actual URL after registration click:", page.url)  

    # Step 4: Select candidate registration
    reg_page.select_candidate_role()
    assert candidate_reg_page.is_at(), "Not on candidate registration page"

    # Step 5: Fill and submit form
    candidate_reg_page.fill_form(
        username="badhonal",
        email="badhonal09@gmail.com",
        password="badhonal09@#", 
        confirm_password="badhonal09@#",
    )

    page.wait_for_timeout(2000)  
    
    # Step 6: Submit form
    candidate_reg_page.submit_registration()
    print("Registration process completed successfully")


