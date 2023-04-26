# Import the required libraries
from selenium import webdriver
import pytest

# Define a fixture that sets up and tears down the WebDriver
@pytest.fixture
def browser():
    # Create a Chrome WebDriver instance
    driver = webdriver.Chrome()
    # Yield the driver object so that the test can use it
    yield driver
    # Close the WebDriver after the test completes
    driver.quit()

# Define the test case that uses the WebDriver fixture
def test_website(browser):
    # Navigate to the example.com website
    browser.get("https://www.example.com")
    try:
        # Check if the title of the page contains the expected text
        assert "Example Domain" in browser.title
    except AssertionError:
        # Add any code here that should be executed if the assertion fails
        print("Assertion failed: 'Example Domain' not found in title")
        # Re-raise the exception so that the test fails
        raise

# Define another test case that visits a different website
def test_google(browser):
    # Navigate to the google.com website
    browser.get("https://www.google.com")
    try:
        # Check if the title of the page contains the expected text
        assert "Google" in browser.title
    except AssertionError:
        # Add any code here that should be executed if the assertion fails
        print("Assertion failed: 'Google' not found in title")
        # Re-raise the exception so that the test fails
        raise