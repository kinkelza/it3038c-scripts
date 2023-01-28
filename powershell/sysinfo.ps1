function getIP{
    (get-netipaddress).ipv4address | Select-String "192.*"
}

$IP = getIP
$USER = $env:USERNAME
$HOST2 =  $env:COMPUTERNAME
$VERSION = $PSVersionTable.PSVersion
$DATE = Get-Date -Format "MM-dd-yyyy"

$BODY = "This machine's IP is $IP, User is $USER, Host is $HOST2, Powershell Version is $VERSION, Today Is $DATE"


# Write-Host($BODY)
Send-MailMessage -To "leonardf@ucmail.uc.edu" -From "zkinkelaar@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)


