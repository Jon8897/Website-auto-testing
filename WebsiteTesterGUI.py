# Import the required libraries
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
import WebsiteTester

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

    def __del__(self):
        # Close the browser when the GUI is closed
        if self.browser:
            self.browser.quit()

# Create the GUI window
root = tk.Tk()
root.geometry("300x200")
website_tester_gui = WebsiteTesterGUI(root)
root.mainloop()