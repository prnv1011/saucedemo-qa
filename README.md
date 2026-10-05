SauceDemo - Playwright Automation

About

This project contains one end-to-end automated test for the SauceDemo application using Python, Playwright and Pytest.
The test covers the main purchase flow from login to successful order completion.

Automated Flow

The test performs the following steps:

Login using the standard user.
Verify successful login.
Add Sauce Labs Backpack to the cart.
Open the cart and verify the product.
Proceed to checkout.
Enter customer details.
Verify the product on the checkout overview.
Complete the order.
Verify the order confirmation message.

Automation Approach

I used a simple Page Object Model to keep page-specific locators and actions separate from the test flow.

The test itself focuses on the complete user journey, while the page classes handle the actions for each application page.