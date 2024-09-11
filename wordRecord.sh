hasCommandByType(){
    if type $1 2>/dev/null; then
        echo 1
    else 
        echo 0
    fi
}

result=$(hasCommandByType countzh)
result=$(echo $result | grep is)
if test -z "$result" ; then
    echo "countzh not install, start install"
    go install github.com/kuangcp/gobase/toolbox/countzh@latest
fi

logFile=submission.log

if [ "$1"z = "z" ];then
    word=$(countzh -s) 
    line=$(git ls-files | grep -v "ARTS" | xargs cat | wc -l)
    # echo "$word $line lines on $time " >> $logFile
    echo "$word $line lines" >> $logFile
else
	less $logFile
fi
