# Import Selenium module
Import-Module Selenium

# Start new web driver
try {
    $driver = Start-SeChrome
}
Catch {
    Write-Host "Error starting web driver : $_"
    return
}

# Navigate website
try {
    $driver.Navigate().GoToUrl("https://www.example.com")
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

