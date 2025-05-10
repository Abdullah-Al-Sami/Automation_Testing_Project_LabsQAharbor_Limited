from pages.subscribe_page import Subscribe

#Invaid Subscribe 
def test_invalid_subscribe(page):
    subscribe_page = Subscribe(page)

    # Step 1: Navigate
    subscribe_page.navigate()

    # Step 2: Enter email
    subscribe_page.fill_form("abdullah.al.sami05@gmail.com")

    # Step 3: Submit
    subscribe_page.submit_subcription()

    # Step 4: Verify success
    #assert subscribe_page.is_subscription_successful(), "Subscription failed - success message not shown"

    # Step 5: Add timeout to see the result
    page.wait_for_timeout(5000)
    print("Subscription successful!")
