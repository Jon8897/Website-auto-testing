## Idea

First, let's start with defining the requirements and goals of the automated website tester. What kind of website are you testing? What are the specific scenarios you want to test? What kind of data or feedback do you want to get from the test results?

Once we have a clear understanding of the goals and requirements, we can proceed with developing a test plan. Here are some steps to consider when developing a test plan:

1. Identify the scenarios to be tested: Identify the key user flows and functionalities of the website that need to be tested.
2. Determine the test environment: Decide on the test environment (e.g. test server, production server) and the test data to be used.
3. Develop test cases: Develop test cases for each scenario to be tested, including input data, expected results, and actual results.
4. Automate tests: Develop test scripts to automate the testing process, using a testing framework such as Selenium.
5. Execute tests: Run the tests in the test environment and record the results.
6. Analyze results: Analyze the test results to determine if the website meets the desired quality standards.

### here is a breakdown of the code: ###

1. The first line imports the necessary libraries: **`selenium`** and **`pytest`**.
2. A **`fixture`** named **`browser`** is defined. This fixture sets up and tears down the **`WebDriver`** for the test. It creates a **`Chrome`** WebDriver instance and yields the driver object so that the test can use it. After the test completes, the fixture closes the **`WebDriver`**.
3. A **`test`** function named **`test_website`** is defined that takes the **`browser`** fixture as a parameter.
4. The **`browser`** is directed to the **`https://www.example.com`** website.
5. An assertion is made to check if the title of the page contains the expected text "Example Domain".
6. If the assertion fails, an error message is printed and the exception is re-raised so that the test fails.

Overall, this code sets up a **`WebDriver`** using **`selenium`** and **`Chrome`**, navigates to a website, and makes an assertion to verify that the page title contains the expected text. If the assertion fails, an error message is printed and the test fails.

## Updates Made

### 27/04/2023 ###

- Removed section of google.com check
- Added specific url looking 
- Added a log for improvements

## Update Ideas

- Create A GUI with input to make sure friendly website tester
- Add more functions to test 
- Being able to test CMS pages
- Look for bugs in code 
- Check all functionality of code 