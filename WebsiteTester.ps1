# Load GUI from XAML
Add-Type -AssemblyName PresentationFramework

$xamlFile = "C:\Users\jonathankeefe.ASTONBERKELEY\OneDrive - Aston Berkeley Systems Ltd\Desktop\Projects\git-projects\Website-auto-testing\WebsiteTesterGUI.xaml"
$stream = New-Object IO.FileStream $xamlFile, [System.IO.FileMode]::Open
$xamlReader = New-Object System.Windows.Markup.XamlReader
$window = $xamlReader.Load($stream)

# Get UI elements
$txtUrl = $window.FindName("txtUrl")
$btnTestWebsite = $window.FindName("btnTestWebsite")

# Event handler for "Test Website" button
$btnTestWebsite.Add_Click({
    # Get URL from input
    $url = $txtUrl.Text

    # Import Selenium module
    Import-Module Selenium

    # Start new web driver
    try {
        $chromeOptions = New-Object OpenQA.Selenium.Chrome.ChromeOptions
        $chromeOptions.AcceptInsecureCertificates = $true
        $driver = Start-SeChrome -ChromeOptions $chromeOptions
    }
    Catch {
        Write-Host "Error starting web driver : $_"
        return
    }

    # Navigate website
    try {
        $driver.Navigate().GoToUrl($url)
    }
    catch {
        Write-Host "Error navigating website: $_"
        $driver.Close()
        return
    }

    # Find an element on the page  
    try {
        $searchBox = $driver.FindElementByName("search")
    }
    catch {
        Write-Host "Error finding search box: $_"
        $driver.Close()
        return
    }

    # Enter search query
    try {
        $searchBox.SendKeys("example")
    }
    catch {
        Write-Host "Error entering search query: $_"
        $driver.Close()
        return
    }

    # Submit search query
    try {
        $searchBox.Submit()
    }
    catch {
        Write-Host "Error submitting search query: $_"
        $driver.Close()
        return
    }

    # Wait for search results to load
    try {
        $driver.WaitForElementByName("search-results", 10)
    }
    catch {
        Write-Host "Error waiting for search results: $_"
        $driver.Close()
        return
    }

    # Check search results
    try{
        $searchResults = $driver.FindElementByName("search-results")
        if ($searchResults.Displayed) {
            Write-Host "Search results found"
        } else {
            Write-Host "Search results not found"
        }
    }
    catch {
        Write-Host "Error checking search results: $_"
    }

    # Close web driver
    $driver.Close()

})

# Show GUI
$window.ShowDialog() | Out-Null