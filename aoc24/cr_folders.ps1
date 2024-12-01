$start = [int](Read-Host "Enter the starting number")
$end = [int](Read-Host "Enter the ending number")

for ($i = $start; $i -le $end; $i++) {
    $folderName = "day$i"
    New-Item -ItemType Directory -Path $folderName -Force

    # Create src.py with correct formatting
    $srcContent = @"
import sys
with open(sys.argv[1],'r') as f:
    pass
"@
    $srcContent | Out-File -FilePath "$folderName\src.py" -Encoding utf8

    # Create empty input.txt and test.txt
    New-Item -ItemType File -Path "$folderName\input.txt" | Out-Null
    New-Item -ItemType File -Path "$folderName\test.txt" | Out-Null
}


Write-Host "Folders from day$start to day$end with files src.py, input.txt, and test.txt have been created."
