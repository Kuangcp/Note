logFile=submission.log

if [ "$1"z = "z" ];then
    word=$(count -s) 
    line=$(git ls-files | xargs cat | wc -l)
    time=$(date "+%F %T")
    echo "$word $line lines on $time " >> $logFile
	less $logFile
else 
	less $logFile
fi
