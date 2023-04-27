# Import the required libraries
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
import pytest
import logging
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

        # Test the website and display the result
        try:
            WebsiteTester.test_website(url, title)
            messagebox.showinfo("Success", "Website test passed!")
        except:
            logging.error(f"An error occurred while testing {url}")
            messagebox.showerror("Error", "Website test failed. Please check logs for details.")

# Create the GUI window
root = tk.Tk()
root.geometry("300x200")
website_tester_gui = WebsiteTesterGUI(root)
root.mainloop()