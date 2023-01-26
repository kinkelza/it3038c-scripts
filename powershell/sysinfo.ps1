function getIP{
    (get-netipaddress).ipv4address | Select-String "192*"
}

$IP = getIP
$USER = $env:USERNAME
$HOST2 =  $env:COMPUTERNAME
$VERSION = $PSVersionTable.PSVersion
$DATE = Get-Date -DisplayHint Date

$BODY = "This machine's IP is $IP, User is $USER, Host is $HOST2, Powershell Version is $VERSION, Today Is $DATE"


Write-Host($BODY)
