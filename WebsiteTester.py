# Import the required libraries
from selenium import webdriver
import pytest
import logging

# Define a fixture that sets up and tears down the WebDriver
@pytest.fixture
def browser():
    # Create a Chrome WebDriver instance
    driver = webdriver.Chrome()
    # Yield the driver object so that the test can use it
    yield driver
    # Close the WebDriver after the test completes
    driver.quit()

# Set up logging configuration
logging.basicConfig(filename='website-improvements.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

# Define the test case that uses the WebDriver fixture
def test_website(browser, url, title):
    # Navigate to the specified website
    browser.get(url)
    try:
        # Check if the title of the page contains the expected text
        assert title in browser.title
    except AssertionError:
        # Log the error message to the file
        logging.error(f"'{title}' not found in the title of {url}")
        # Re-raise the exception so that the test fails
        raise
