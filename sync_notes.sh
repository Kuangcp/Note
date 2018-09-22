NotePath=/home/kcp/Note/Notes/

cd $NotePath 

cd ..

git clone --depth 1 https://gitee.com/gin9/Memo.git Temp

cd Temp

rm -rf .git/

cd ..

cp -r Temp/* Notes/

rm -rf Temp


