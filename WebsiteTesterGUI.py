# Import the required libraries
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
import pytest
import logging
import WebsiteTester
from urllib.parse import urlparse

class WebsiteTesterGUI:
    def __init__(self, master):
        # Set up the GUI window
        self.master = master
        master.title("Website Tester")

        # Add URL label and entry
        self.url_label = tk.Label(master, text="URL:")
        self.url_label.pack()
        self.url_entry = tk.Entry(master)
        self.url_entry.pack()

        # Add Title label and entry
        self.title_label = tk.Label(master, text="Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(master)
        self.title_entry.pack()

        # Add Test Website button
        self.test_button = tk.Button(master, text="Test Website", command=self.test_website)
        self.test_button.pack()

        # Add Navigation buttons
        self.home_button = tk.Button(master, text="Home", command=self.navigate_home)
        self.home_button.pack()

        self.about_button = tk.Button(master, text="About", command=self.navigate_about)
        self.about_button.pack()

        # Create a browser instance
        self.browser = None 

    def test_website(self):
        # Get the URL and Title entered by the user
        url = self.url_entry.get()
        title = self.title_entry.get()

        # Check if URL and Title fields are empty
        if not url:
            messagebox.showerror("Error", "Please enter a URL")
            return

        if not title:
            messagebox.showerror("Error", "Please enter a title")
            return

        # Check if the URL has a valid format
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            messagebox.showerror("Error", "Invalid URL format")
            return 
        
        # 
        
        # Create a Chrome WebDriver instance if not already created
        if not self.browser:
            self.browser = webdriver.Chrome()

        # Test the website and display the result
        try:
            WebsiteTester.test_website(browser, url, title)
            messagebox.showinfo("Success", "Website test passed!")
        except Exception as e:
            error_message = str(e)
            logging.error(f"An error occurred while testing {url}: {error_message}")
            messagebox.showerror("Error", f"Website test failed. Error: {error_message}.Please check logs for details.")

    def navigate_home(self):
        # Set the URL and Title entries for the Home page
        self.url_entry.delete(0, tk.END)
        self.url_entry.insert(0, "https://www.example.com/home")
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, "Home Page")

    def navigate_about(self):
        # Set the URL and Title entries for the About page
        self.url_entry.delete(0, tk.END)
        self.url_entry.insert(0, "https://www.example.com/about")
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, "About Page")

    def __del__(self):
        # Close the browser when the GUI is closed
        If self.browser:
            self.browser.quit()

# Create the GUI window
root = tk.Tk()
root.geometry("300x200")
website_tester_gui = WebsiteTesterGUI(root)
root.mainloop()