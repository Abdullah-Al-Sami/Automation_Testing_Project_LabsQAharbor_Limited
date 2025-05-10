from pages.home_page import HomePage
from pages.social_pages import SocialPages


# Test : 1 for LinkedIn page navigation
def test_linkedin(page):
    home_page = HomePage(page)
    social_pages  = SocialPages(page)

    # Step 1: Navigate
    home_page.navigate()
    # Step 2:go to linkedin page
    home_page.click_linkdedin_page()

    # Step 3: Verify account page elements
    social_pages.navigate()
    #print("Current URL:", page.url)


    #Step 4: add timeout to see the result
    page.wait_for_timeout(5000)
    print("Page Shows successfully!")

# Test : 2 for Facebook page navigation
def test_facebook(page):
    home_page = HomePage(page)
    social_pages  = SocialPages(page)

    # Step 1: Navigate
    home_page.navigate()
    # Step 2: go to linkedin page
    home_page.click_facebook_page()

    # Step 3: Verify account page elements
    social_pages.navigate1()
    #print("Current URL:", page.url)

    #Step 4: add timeout to see the result
    page.wait_for_timeout(5000)
    print("Page Shows successfully!")