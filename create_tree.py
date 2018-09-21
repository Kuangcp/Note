import os
import sys
import getopt
import subprocess
import fire

red='\033[0;31m'
green='\033[0;32m'
yellow='\033[0;33m'
blue='\033[0;34m'
purple='\033[0;35m'
cyan='\033[0;36m'
white='\033[0;37m'
end='\033[0m'


'''
    通过运行脚本，读取文件夹的文件生成目录，为了gitbook和wiki
    使用： python3 create_tree.py -h 查看帮助
'''
# 忽略的文件夹
ignoreFolder=['.git', 'backup', '.vscode']
# 所有要被忽略的文件
ignoreFile=['PULL_REQUEST_TEMPLATE.md', 'ISSUE_TEMPLATE.md', 'CODE_OF_CONDUCT.md','README.md', 
    'Readme.md', 'CSS3.md', 'HTML5.md', '_Sidebar.md']

result = []

def logError(msg):
    print('%s%s%s'%(red, msg, end))

def logInfo(msg):
    print('%s%s%s'%(green, msg, end))

def printParam(verb, args, comment):
    print('  %s%-5s %s%-6s %s%s'%(green, verb, yellow, args, end, comment))

def help():
    print('run: %s  %s <verb> %s <args>%s'%('create_tree.py', green, yellow, end))
    printParam('-h', '', 'help')
    printParam('-s', '', 'show catalog')
    printParam('-a', '', 'append cataloag to SUMMARAY.md')

# 列出所有文件的列表 并排好序
def listFiles(name):
    lists = []
    dir_list = []
    temp = os.listdir(name)
    temp.sort()
    for r in temp:
        if(not os.path.isdir(name+'/'+r)):
            lists.append(r)
        else:
            dir_list.append(r)
    lists.sort()
    lists = dir_list + lists
    return lists 
        
# 处理文件
def handlerFile(name, count, path):
    temp = '    '*count
    if not name in ignoreFile:
        result.append(temp+'* [ '+name[:-3]+' ](/'+path+')')

# 处理标题(文件夹)
def handlerFolder(name, count):
    temp = '    '*(int(count)-1)
    result.append(temp+'* 【 '+name+' 】') 

# 递归 读取文件夹
def readFolder(name, count):
    handlerFolder(name,count)
    for fold in listFiles(name):
        if fold in ignoreFolder:
            continue
        if not os.path.isdir(name+'/'+fold):
            handlerFile(fold, count, name+'/'+fold)
        else:
            readFolder(name+'/'+fold, count+1)

def readAll():
    Folders = os.listdir('./')
    Folders.sort()
    # 处理根目录下的md文件
    for fold in Folders:
        if fold.endswith('.md') and not fold in ignoreFile:
            result.append("* [ "+fold[:-3]+" ](./"+fold+")")
    # 得到根目录下所有文件夹，然后开始递归得到所有文件       
    for fold in Folders:
        if os.path.isdir(fold) and not fold in ignoreFolder :
            readFolder(fold, 1)

def main(verb=None):
    if verb == '-h':
        help()
        return
    # 只在终端输出
    if verb == "-s":
        readAll()
        for res in result:
            print(res)
    # 追加到SUMMARY
    if verb == "-a":
        readAll()
        subprocess.call('mv SUMMARY.md SUMMARY.md.bak',shell=True)
        with open('SUMMARY.md','w+') as dest:
            dest.write('# Summary\n\n* [ Introduction ](README.md)\n\n')
            for res in result:
                dest.write(res+'\n')
        logInfo('重新生成目录树完成!')

fire.Fire(main)
