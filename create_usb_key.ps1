Param(
    [string]$Drive = 'E:'
)

$out = Join-Path -Path $Drive -ChildPath 'usb.key'
if (Test-Path $out) {
    $ans = Read-Host "$out exists. Overwrite? (y/N)"
    if ($ans -ne 'y') { Write-Output 'Aborted.'; exit 1 }
}

$bytes = New-Object byte[] 32
$provider = New-Object System.Security.Cryptography.RNGCryptoServiceProvider
$provider.GetBytes($bytes)
[IO.File]::WriteAllBytes($out, $bytes)
Write-Output "Created $out"
