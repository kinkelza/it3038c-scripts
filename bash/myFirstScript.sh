#greeting="This is a script. Hello!"
#echo $greeting, thanks for joining us!
#echo '$greeting, thanks for joining us! You owe me $20'
#echo "$greeting, thanks for joining us!"
#echo "$greeting, you owe me \$20"

#p2
echo =========NEW SCRIPT========
echo Machine Type: $MACHTYPE
echo Hostname: $HOSTNAME
echo Working Directory: $PWD
echo Session Length: $SECONDS
echo Home Directory: $HOME
a=$(ip a | grep 'ens192' | awk '{print $2}')
echo My IP is $a

