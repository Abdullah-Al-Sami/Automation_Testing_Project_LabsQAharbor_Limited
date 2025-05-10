from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.acc_page import Acc_Page
from pages.single_findjobs_page import SingleFindjobsPage
from pages.single_bookmark_jobpage import SingleBookmarkJobPage
from pages.job_details_page import JobDetailsPage
from pages.logout_page import LogoutPage
from pages.remove_job import RemoveJobPage


#valid Book mark jobs - 1
def test_remove_bookmarked_job(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    account_page = AccountPage(page)
    #acc_page= Acc_Page(page)
    single_find_jobs_page = SingleFindjobsPage(page)
    single_bookmark_job_page = SingleBookmarkJobPage(page)
    job_details_page = JobDetailsPage(page)
    remove_job = RemoveJobPage(page)
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
    assert single_find_jobs_page.is_at(), "Find Job page not loaded"

    # Step 6: Navigate and click for bookmark any jobs in findjobs page
    single_find_jobs_page.bookmark_jobs()

    #step 7: Verify bookmark job to show in my account page
    single_find_jobs_page.goto_myaccount()
    assert account_page.is_at(), "Account page not loaded after job find job page"
    print("Current URL:", page.url)

    #step 8: Verify job bookmarked to click save and view job details
    account_page.show_bookmark_jobs()
    assert single_bookmark_job_page.is_at(), "Bookmarked job not loaded"
    print("Current URL:", page.url)


    page.wait_for_timeout(3000) 
    remove_job.remove_bookmarked_job()
    assert remove_job.get_current_url(), "Bookmarked job details not loaded"
    print("Current URL:", page.url)
    page.wait_for_timeout(3000) 
    print("Job removed successfully")
    
    # Step 13: Navigate and click for logout
    account_page.log_out()
    assert log_out_page.get_current_url(), "Logout page not loaded"
    print("Current URL:", page.url)

    #step 14: Verify logout process
    page.wait_for_timeout(3000)  
    print("Successfully Logged out")




#valid Book mark jobs - 2
def test_remove_bookmarked_job1(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    account_page = AccountPage(page)
    #acc_page= Acc_Page(page)
    single_find_jobs_page = SingleFindjobsPage(page)
    single_bookmark_job_page = SingleBookmarkJobPage(page)
    job_details_page = JobDetailsPage(page)
    remove_job = RemoveJobPage(page)
    log_out_page = LogoutPage(page)

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
    
    # Verify account page elements
    assert account_page.is_at(), "Account page not loaded after login"
    print("Current URL:", page.url)
    
    print("Login successful!")

    # Step 5: Navigate and click for find jobs in findjobs page
    account_page.find_jobs()
    assert single_find_jobs_page.is_at(), "Find Job page not loaded"

    # Step 6: Navigate and click for bookmark any jobs in findjobs page
    single_find_jobs_page.bookmark_jobs()

    #step 7: Verify bookmark job to show in my account page
    single_find_jobs_page.goto_myaccount()
    assert account_page.is_at(), "Account page not loaded after job find job page"
    print("Current URL:", page.url)

    #step 8: Verify job bookmarked to click save and view job details
    account_page.show_bookmark_jobs()
    assert single_bookmark_job_page.is_at(), "Bookmarked job not loaded"
    print("Current URL:", page.url)


    page.wait_for_timeout(3000) 
    remove_job.remove_bookmarked_job()
    assert remove_job.get_current_url(), "Bookmarked job details not loaded"
    print("Current URL:", page.url)
    page.wait_for_timeout(3000) 
    print("Job removed successfully")
    
    # Step 13: Navigate and click for logout
    account_page.log_out()
    assert log_out_page.get_current_url(), "Logout page not loaded"
    print("Current URL:", page.url)

    #step 14: Verify logout process
    page.wait_for_timeout(3000)  
    print("Successfully Logged out")
