from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.findjobs_page import FindjobsPage
from pages.bookmark_jobpage import BookmarkJobPage
from pages.job_details_page import JobDetailsPage
from pages.logout_page import LogoutPage

#Valid Book mark jobs
def test_bookmarked_job_details(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    account_page = AccountPage(page)
    find_jobs_page = FindjobsPage(page)
    bookmark_job_page = BookmarkJobPage(page)
    job_details_page = JobDetailsPage(page)
    log_out_page = LogoutPage(page)

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
    
    # Verify account page elements
    assert account_page.is_at(), "Account page not loaded after login"
    print("Current URL:", page.url)
    
    print("Login successful!")

    # Step 5: Navigate and click for find jobs in findjobs page
    account_page.find_jobs()
    assert find_jobs_page.is_at(), "Find Job page not loaded"

    # Step 6: Navigate and click for bookmark any jobs in findjobs page
    find_jobs_page.bookmark_jobs()

    #step 7: Verify bookmark job to show in my account page
    find_jobs_page.goto_myaccount()
    assert account_page.is_at(), "Account page not loaded after job find job page"
    print("Current URL:", page.url)

    #step 8: Verify job bookmarked to click save and view job details
    account_page.show_bookmark_jobs()
    assert bookmark_job_page.is_at(), "Bookmarked job not loaded"
    print("Current URL:", page.url)

    #step 9: View job details
    bookmark_job_page.view_job_details()
    assert job_details_page.get_current_url(), "Bookmarked job details not loaded"
    print("Current URL:", page.url)
    

    page.wait_for_timeout(3000)  
    print("Bookmmarked Job viewed successfully")


    # Step 10: Navigate and click for logout
    account_page.log_out()

    assert log_out_page.get_current_url(), "Logout page not loaded"
    print("Current URL:", page.url)

    #step 11: Verify logout process
    page.wait_for_timeout(3000)  
    print("Successfully Logged out")



#Valid Bookmark Jobs

def test_bookmarked_job_details1(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    account_page = AccountPage(page)
    find_jobs_page = FindjobsPage(page)
    bookmark_job_page = BookmarkJobPage(page)
    job_details_page = JobDetailsPage(page)
    log_out_page = LogoutPage(page)

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
    
    # Verify account page elements
    assert account_page.is_at(), "Account page not loaded after login"
    print("Current URL:", page.url)
    
    print("Login successful!")

    # Step 5: Navigate and click for find jobs in findjobs page
    account_page.find_jobs()
    assert find_jobs_page.is_at(), "Find Job page not loaded"

    # Step 6: Navigate and click for bookmark any jobs in findjobs page
    find_jobs_page.bookmark_jobs()

    #step 7: Verify bookmark job to show in my account page
    find_jobs_page.goto_myaccount()
    assert account_page.is_at(), "Account page not loaded after job find job page"
    print("Current URL:", page.url)

    #step 8: Verify job bookmarked to click save and view job details
    account_page.show_bookmark_jobs()
    assert bookmark_job_page.is_at(), "Bookmarked job not loaded"
    print("Current URL:", page.url)

    #step 9: View job details
    bookmark_job_page.view_job_details()
    assert job_details_page.get_current_url(), "Bookmarked job details not loaded"
    print("Current URL:", page.url)
    

    page.wait_for_timeout(3000)  
    print("Bookmmarked Job viewed successfully")


    # Step 10: Navigate and click for logout
    account_page.log_out()

    assert log_out_page.get_current_url(), "Logout page not loaded"
    print("Current URL:", page.url)

    #step 11: Verify logout process
    page.wait_for_timeout(3000)  
    print("Successfully Logged out")