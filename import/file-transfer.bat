echo %DATE%_%TIME% >> "./Logs/database-load-%1.log"
echo "Fetching file from RPi Server: tweet_data_%1.json" >> "./Logs/database-load-%1.log"

echo open sftp://pi:raspberry@192.168.0.25 -hostkey="ssh-rsa 2048 7a:46:e5:c7:f0:8c:e7:3f:87:37:6b:00:cd:a3:b3:2b" >> ftpcmd.dat
echo get /home/pi/jules/retweeter/furzedown/export/tweet_data_%1.json ..\export\ >> ftpcmd.dat
echo exit >> ftpcmd.dat

"C:\Program Files (x86)\WinSCP\winscp.com" /script=ftpcmd.dat
del ftpcmd.dat
