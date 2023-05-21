# Import the required libraries
import traceback
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

    # Log the actual title of the page
    actual_title = browser.title
    logging.info(f"Actual title {url}: {actual_title}")

    try:
        # Check if the title of the page contains the expected text
        assert title in browser.title
    except AssertionError:
        # Log the error message to the file
        logging.error(f"'{title}' not found in the title of {url}")
        # log the full traceback of the exception
        logging.error(traceback.format_exc())
        # Re-raise the exception so that the test fails
        raise

def navigate_home(self):
        try:
            # Read the URL from the URL entry field 
            url = self.url_entry.get()

            # Log the navigation action
            logging.info(f"Navigating to Home page with URL: {url}")

            # Set the URL and Title entries for the Home page
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, url + "/home")
            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, "Home Page")
        except Exception as e:
            logging.error(f"An error occurred during navigation to Home page: {str(e)}")

def navigate_about(self):
        try:
            # Read the URL from the URL entry field 
            url = self.url_entry.get()

            # Log the navigation action
            logging.info(f"Navigating to Home page with URL: {url}")

            # Set the URL and Title entries for the About page
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, url + "/about")
            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, "About Page")
        except Exception as e:
            logging.error(f"An error occurred during navigation to About page: {str(e)}")