hasCommandByType(){
    if type $1 2>/dev/null; then
        echo 1
    else 
        echo 0
    fi
}

result=$(hasCommandByType count)
result=$(echo $result | grep is)
if test -z "$result" ; then
    echo "count not install"
    go get github.com/kuangcp/gobase/count
    cd $GOPATH
    cd github.com/kuangcp/gobase/count
    go install
fi

logFile=submission.log

if [ "$1"z = "z" ];then
    word=$(count -s) 
    line=$(git ls-files | grep -v "ARTS" | xargs cat | wc -l)
    time=$(date "+%F %T")
    echo "$word $line lines on $time " >> $logFile
	less $logFile
else 
	less $logFile
fi
