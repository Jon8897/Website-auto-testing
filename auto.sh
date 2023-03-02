Import-Module Selenium 

#Start new web driver
$driver = Start-SeChrome

#Navigate website
$driver.Navigate().GoToUrl("")

#Finds an element on the page  
$searchBox = $driver.FindElementByName("#")

