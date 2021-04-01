#pass in file if stored in another directory. If run in the context of the folder, default to text file
param (
    $file = 'reverseme.txt'
)
#get content of text file
$text = Get-Content $file
#iterate over the length of the text file contents in reverse. Write host defaults a new line.
for ($i=$text.Length-1; $i -ge 0; $i--) {
    Write-Host $text[$i] -NoNewline
}
