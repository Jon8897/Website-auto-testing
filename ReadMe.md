# UPDATE - Language change to python 

## Auto Website Testing Script

First, let's start with defining the requirements and goals of the automated website tester. What kind of website are you testing? What are the specific scenarios you want to test? What kind of data or feedback do you want to get from the test results?

Once we have a clear understanding of the goals and requirements, we can proceed with developing a test plan. Here are some steps to consider when developing a test plan:

1. Identify the scenarios to be tested: Identify the key user flows and functionalities of the website that need to be tested.
2. Determine the test environment: Decide on the test environment (e.g. test server, production server) and the test data to be used.
3. Develop test cases: Develop test cases for each scenario to be tested, including input data, expected results, and actual results.
4. Automate tests: Develop test scripts to automate the testing process, using a testing framework such as Selenium.
5. Execute tests: Run the tests in the test environment and record the results.
6. Analyze results: Analyze the test results to determine if the website meets the desired quality standards.

- To run script 

## Whats does it achieve right now 

- The code is trying to test a website by performing a search query and checking the results. The code initializes a new web driver using Selenium and navigates to a website. It then finds a search box on the page, enters a search query, submits the query, and waits for the search results to load. Finally, it checks whether the search results are displayed and outputs a message indicating whether the results were found or not.

### Updates

- Shows errors
- Identify where the errors are in the code 
- Checks whole website and functionality 
- Looks for vulnerabilities 
- Run with a GUI
- Logs all issues fo a website

### Errors

#### 24/04/2023 ####

- It looks like there are several issues with the code. The first error message suggests that the version of the ChromeDriver being used does not support the version of Chrome installed on the system. You may need to download and install the correct version of ChromeDriver for your version of Chrome.

- The subsequent error messages indicate that the web driver object is null and cannot be used to perform actions on the webpage. This could be due to an issue with the ChromeDriver installation, or with the way the web driver object is being initialized and used in the code.

- It's also possible that there is an issue with the website being tested, or with the specific elements being accessed in the code. You may need to adjust the code to use different methods for locating and interacting with the elements on the page.

- Overall, it may be helpful to troubleshoot the issues one by one, starting with the ChromeDriver installation and initialization, and then moving on to the specific actions being performed on the webpage.

- GUI not running find fix

#### 25/04/2023 ####

- The first error is caused by the script attempting to convert a value to a type that is incompatible. Specifically, it is trying to convert "[System.IO.FileMode]::Open" to the "System.IO.FileMode" type, but it cannot match it to a valid enumerator name.

- The second error is stating that the method "Load" does not exist in the "System.Windows.Markup.XamlReader" class.

- The third, fourth and fifth errors are all caused by the variable "$window" being null. This means that the script is unable to find the XAML window and is therefore unable to retrieve the UI elements.

- The final error is also caused by the null variable "$window". The script is trying to call the "ShowDialog()" method on this null variable, which is causing an error.

- Error with loading chrome drive

### Fixes To-do

#### 24/04/2023 ####

1. Check the version of Chrome installed on your system, and download and install the corresponding version of ChromeDriver from the official website.

2. Double-check the syntax and formatting of the code to make sure there are no errors or typos that could be causing issues.

3. Verify that the website being tested is functioning correctly, and that the specific elements being accessed in the code are valid and accessible.

4. Try using different methods for locating and interacting with elements on the page, such as using CSS selectors or XPath expressions.

5. Add error-handling code to catch and handle any exceptions that may be thrown during the execution of the script.

#### 25/04/2023 ####

1. The first error is because PowerShell is unable to convert the string "[System.IO.FileMode]::Open" to the type "System.IO.FileMode". You can try using the value "Open" directly, like this:

<pre>
$stream = New-Object IO.FileStream $xamlFile, Open, Read
</pre>

2. The second error is because the XamlReader object does not have a method called "Load". This is likely because you are using an older version of .NET. You can try using the "LoadXml" method instead:

<pre>
$xaml = Get-Content $xamlFile -Raw
$stream = New-Object IO.MemoryStream([System.Text.Encoding]::UTF8.GetBytes($xaml))
$window = $xamlReader.LoadXml($stream)
</pre>

3. For the remaining errors, it seems that the UI elements are not being found by the script. You should ensure that the XAML file contains elements with the correct names.

4. Update Selenium

### Issue

#### 24/04/2023 ####

- Error starting web driver : Exception calling ".ctor" with "2" argument(s): "session not created: This version of ChromeDriver only supports Chrome version 83 (SessionNotCreated)"

    - Resolution:
        1. Determine the version of Chrome you have installed. You can find this information by opening Chrome and navigating to the "Help" menu > "About Google Chrome".
        2. Download the corresponding version of ChromeDriver from the official website: https://chromedriver.chromium.org/downloads.
        3. Replace the existing version of ChromeDriver with the newly downloaded version in your script or environment. Make sure to update the path to the ChromeDriver executable in your code if necessary.
        4. Re-run your script and confirm that the error has been resolved.

## Test images coming soon