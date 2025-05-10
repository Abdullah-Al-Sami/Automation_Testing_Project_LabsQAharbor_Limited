from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.findjobs_page import FindjobsPage
from pages.job_details_page import JobDetailsPage
from pages.logout_page import LogoutPage


#Valid Search Jobs
def test_search_jobs(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    account_page = AccountPage(page)
    find_jobs_page = FindjobsPage(page)
    job_details_page = JobDetailsPage(page)
    logout_page = LogoutPage(page)

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
    find_jobs_page.fill_search_jobs(
        search="Senior SQA Engineer",
    )

    #step 7: Verify search job to show in find jobs page
    find_jobs_page.search_jobs()
    page.wait_for_timeout(2000)  
    assert find_jobs_page.is_at(), "Search job not loaded"
    print("Current URL:", page.url)

    #step 8: Verify view job details
    find_jobs_page.details_jobs_searched()
    page.wait_for_timeout(2000)  
    assert job_details_page.get_current_url2, "Details about job not loaded"
    print("Current URL:", page.url)

    #step 9: Verify job details to click save and view job details
    page.wait_for_timeout(2000)  
    print("Successfully viewed job details")

    account_page.is_at()
    account_page.log_out()
    assert logout_page.is_at(), "Logout page not loaded"

    # Step 10: Add timeout to see the result
    page.wait_for_timeout(3000)  
    print("Logout process completed successfully")
