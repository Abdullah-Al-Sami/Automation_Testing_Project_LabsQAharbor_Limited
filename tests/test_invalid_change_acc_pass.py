from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.change_password import ChnagePasswordPage
    
#InValid Test change password [Do not have Account]
def test_invalid_change_acc_pass(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    account_page = AccountPage(page)
    change_password = ChnagePasswordPage(page)

    # Step 1: Navigate and click sign-in
    home_page.navigate()
    home_page.click_sign_in()

    # Step 2: Verify login page
    assert login_page.is_at(), "Login page not loaded"

    # Step 3: Enter credentials
    login_page.enter_credentials(
        "qa@gmail.com", 
        "lalal@#"
    )

    # Step 4: Submit and verify
    login_page.submit()
    
    # Step 5: Verify account page elements
    assert account_page.is_at(), "Account page not loaded after login"
    print("Current URL:", page.url)
    
    print("Login successful!")

    # Step 6: Navigate and click change password
    account_page.is_at()
    account_page.change_password()

    assert change_password.is_at(), "Login page not loaded"

    # Step 7: Enter new password 
    change_password.fill_form(

        password="lalal@#", 
        confirm_password="lalal@#",
    )

    change_password.change_password_submit()

    # Step 8: Verify account page elements
    assert change_password.is_at(), "Account page not loaded after login"
    print("Current URL:", page.url)

    # Step 9: Add timeout to see the result
    page.wait_for_timeout(3000)  
    print("Change password process completed successfully")



