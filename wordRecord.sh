logFile=submission.log

if [ "$1"z = "z" ];then
	count -s >> $logFile && date +%y-%m-%d_%H:%M:%S >> $logFile
	echo "------------------------------------------" >> $logFile
	less $logFile
else 
	less $logFile
fi
