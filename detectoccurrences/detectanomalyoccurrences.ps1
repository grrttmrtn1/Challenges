#pass in file if stored in another directory. If run in the context of the folder, default to text file
#add percentvariance as whole number i.e. 90 = 90%
param (
    $file = 'occurences.txt',
    $percentVariance = 90
)

$text = Get-Content $file

#assuming that the result was okay to see rare and common I would display like this 
#$text.ToCharArray() | Group-Object -NoElement | Sort-Object -Property Count

#count characters and group them
$charArray = $text.ToCharArray() | Group-Object -NoElement
#calculate average based upon sum of all counts
$average = ($charArray | Measure-Object -Property Count -Sum).Sum/$charArray.Count
#output all characters with a count with a higher variance than passed. By default higher than a 90% variance.
$charArray | where Count -le ($average * (1 - $percentVariance/100))
