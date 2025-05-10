from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage


#Invalid login 1
def test_invalid_login(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    account_page = AccountPage(page)

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
