from pages.home_page import HomePage


#Run From the home Page:
def test_home_page(page):
    home_page = HomePage(page)
    
    # Step 1: Navigate to the home page
    home_page.navigate()
    
    # Step 2: Verify the URL
    current_url = home_page.get_current_url()
    assert current_url == "https://labsqajobs.qaharbor.com/", \
        f"URL mismatch. Expected: 'https://labsqajobs.qaharbor.com/', Actual: '{current_url}'"
    print(f"Test Passed: Home Page Successfully Displayed ({current_url})")

    # Step 3: add timeout to see the result
    page.wait_for_timeout(5000)
    print("Home page test completed successfully!")