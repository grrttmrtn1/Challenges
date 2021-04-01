#pass in files if stored in another directory. If run in the context of the folder, default to text file
#inFile = input
#outFile = output
param (
    $inFile = 'iplist.txt',
    $outFile = 'results.txt'
)
$text = Get-Content $inFile
#sort by octect and then convert back to string
[string[]]$sortedIPs = [system.version[]]($text) | Sort-Object
#output to file
$sortedIPs | Out-File 'results.txt'
