from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.logout_page import LogoutPage


#valid Logout
def test_logout(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    account_page = AccountPage(page)
    logout_page = LogoutPage(page)

    # Step 1: Navigate and click sign-in
    home_page.navigate()
    home_page.click_sign_in()

    # Step 2: Verify login page
    assert login_page.is_at(), "Login page not loaded"

    # Step 3: Enter credentials
    login_page.enter_credentials(
        "lalala@gmail.com", 
        "Lalala@#"
    )

    # Step 4: Submit and verify
    login_page.submit()
    
    # Step 5: Verify account page elements
    assert account_page.is_at(), "Account page not loaded after login"
    print("Current URL:", page.url)
    
    print("Login successful!")

    # Step 6: Navigate and click for logout
    account_page.is_at()
    account_page.log_out()

    assert logout_page.is_at(), "Logout page not loaded"

    # Step 7: Add timeout to see the result
    page.wait_for_timeout(3000)  
    print("Logout process completed successfully")
