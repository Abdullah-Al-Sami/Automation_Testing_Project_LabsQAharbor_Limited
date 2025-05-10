from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage

#Valid login 1
def test_login(page):
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
        "abdullah.al.sami05@gmail.com", 
        "Abdullah.al.sami05@#"
    )

    # Step 4: Submit and verify
    login_page.submit()
    
    # Step 5: Verify account page elements
    assert account_page.is_at(), "Account page not loaded after login"
    print("Current URL:", page.url)
    
    print("Login successful!")


#valid login 2
def test_login1(page):
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
        "islamsam404@gmail.com", 
        "Islamsam404@#"
    )

    # Step 4: Submit and verify
    login_page.submit()
    
    # Step 5: Verify account page elements
    assert account_page.is_at(), "Account page not loaded after login"
    print("Current URL:", page.url)
    
    print("Login successful!")


    #valid login 3
def test_login2(page):
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
        "lalala@gmail.com", 
        "Lalala@#"
    )

    # Step 4: Submit and verify
    login_page.submit()
    
    # Step 5: Verify account page elements
    assert account_page.is_at(), "Account page not loaded after login"
    print("Current URL:", page.url)
    
    print("Login successful!")
