# Import Selenium module
Import-Module Selenium

# Start new web driver
$driver = Start-SeChrome

# Navigate website
$driver.Navigate().GoToUrl("https://www.astonberkeley.com")

# Find an element on the page  
$searchBox = $driver.FindElementByName("search")

# Enter search query
$searchBox.SendKeys("example")

# Submit search query
$searchBox.Submit()

# Wait for search results to load
$driver.WaitForElementByName("search-results", 10)

# Check search results
$searchResults = $driver.FindElementByName("search-results")
if ($searchResults.Displayed) {
    Write-Host "Search results found"
} else {
    Write-Host "Search results not found"
}

# Close web driver
$driver.Close()

