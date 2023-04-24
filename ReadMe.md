# Auto Website Testing Script

First, let's start with defining the requirements and goals of the automated website tester. What kind of website are you testing? What are the specific scenarios you want to test? What kind of data or feedback do you want to get from the test results?

Once we have a clear understanding of the goals and requirements, we can proceed with developing a test plan. Here are some steps to consider when developing a test plan:

1. Identify the scenarios to be tested: Identify the key user flows and functionalities of the website that need to be tested.
2. Determine the test environment: Decide on the test environment (e.g. test server, production server) and the test data to be used.
3. Develop test cases: Develop test cases for each scenario to be tested, including input data, expected results, and actual results.
4. Automate tests: Develop test scripts to automate the testing process, using a testing framework such as Selenium.
5. Execute tests: Run the tests in the test environment and record the results.
6. Analyze results: Analyze the test results to determine if the website meets the desired quality standards.

- To run script Invoke-Expression '.\website-tester.ps1'

## Updates

- Shows errors
- Identify where the errors are in the code 
- Checks whole website and functionality 
- Looks for vulnerabilities 
- Run with a GUI
- Logs all issues fo a website

## Errors

- It looks like there are several issues with the code. The first error message suggests that the version of the ChromeDriver being used does not support the version of Chrome installed on the system. You may need to download and install the correct version of ChromeDriver for your version of Chrome.

- The subsequent error messages indicate that the web driver object is null and cannot be used to perform actions on the webpage. This could be due to an issue with the ChromeDriver installation, or with the way the web driver object is being initialized and used in the code.

- It's also possible that there is an issue with the website being tested, or with the specific elements being accessed in the code. You may need to adjust the code to use different methods for locating and interacting with the elements on the page.

- Overall, it may be helpful to troubleshoot the issues one by one, starting with the ChromeDriver installation and initialization, and then moving on to the specific actions being performed on the webpage.

## Fixes To-do

1. Check the version of Chrome installed on your system, and download and install the corresponding version of ChromeDriver from the official website.

2. Double-check the syntax and formatting of the code to make sure there are no errors or typos that could be causing issues.

3. Verify that the website being tested is functioning correctly, and that the specific elements being accessed in the code are valid and accessible.

4. Try using different methods for locating and interacting with elements on the page, such as using CSS selectors or XPath expressions.

5. Add error-handling code to catch and handle any exceptions that may be thrown during the execution of the script.

## Test images coming soon