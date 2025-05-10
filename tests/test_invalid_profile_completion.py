from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.logout_page import LogoutPage
from pages.update_profile_page import UpdateProfilePage
from pathlib import Path

# Test file paths - update these with your actual file paths
TEST_CV_PATH = "tests/information/MdAbdullahAlSami.pdf"
TEST_IMAGE_PATH = "tests/information/sami.png"


#Invalid Profile Completion - Already Created
def test_invalid_profile_completion(page):
    # Verify test files exist before starting
    if not Path(TEST_IMAGE_PATH).exists():
        raise FileNotFoundError(f"Profile image not found at {TEST_IMAGE_PATH}")
    if not Path(TEST_CV_PATH).exists():
        raise FileNotFoundError(f"CV file not found at {TEST_CV_PATH}")

    home_page = HomePage(page)
    login_page = LoginPage(page)
    account_page = AccountPage(page)
    update_profile_page = UpdateProfilePage(page)
    logout_page = LogoutPage(page)

    # Step 1: Navigate and authenticate
    home_page.navigate()
    home_page.click_sign_in()
    assert login_page.is_at(), "Login page not loaded"
    
    # Login with credentials
    login_page.enter_credentials(
        "islamsam404@gmail.com", 
        "Islamsam404@#"
    )
    login_page.submit()
    
    assert account_page.is_at(), "Account page not loaded after login"
    print("Login successful!")

    # Step 2: Navigate to profile update
    account_page.edit_profile()
    account_page.edit_profile_page()
    page.wait_for_timeout(3000)
    assert update_profile_page.is_at(), "Update profile page not loaded"

    # Step 3: Fill in profile information
    update_profile_page.enter_credentials(
        firstname="Md. Abdullah", 
        lastname="Al Sami", 
        mobile="+8801954596163",  
        portfolio="https://www.linkedin.com/in/md-abdullah-al-sami-3b926a24a/", 
        listenqa="Yes, heard for best SQA Industry"
    )
     # Step 6: Enter experience
    update_profile_page.enter_experience()

    #Step 7: Wait for the "Yes" radio button to be selected
    update_profile_page.select_yes()


    #Step 8: Upload files picture and CV
    page.wait_for_timeout(5000)
    #Replace individual uploads with:
    update_profile_page.upload_files(TEST_IMAGE_PATH, TEST_CV_PATH)

    update_profile_page.submit_profile_updatation()

    # Step 9: Logout
    account_page.log_out()
    assert logout_page.is_at(), "Logout failed"
    print("Successfully Logged out")
