# Load GUI from XAML
Add-Type -AssemblyName WindowsBase

[xml]$xaml = Get-Content "WebsiteTesterGUI.xaml"
$reader = New-Object System.Xml.XmlNodeReader($xaml)
$window = [Windows.Markup.XamlReader]::Load($reader)
Add-Type -AssemblyName PresentationFramework

# Get UI elements
$btnTestWebsite = $window.FindName("btnTestWebsite")

# Event handlers
$btnTestWebsite.Add_Click({
    # Run website tester script
    & ".\WebsiteTester.ps1"
})

# Show GUI
$window.ShowDialog() | Out-Null