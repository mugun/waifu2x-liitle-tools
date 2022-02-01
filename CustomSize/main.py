import file
import tools
import Waifu2xExec
import sys
import shutil

if __name__ == '__main__':
    list=tools.GetArg(sys.argv[1:])
    waifu2xexec= list.get("execute")
    output= list.get("output")
    path = file.filePath(list.get("input"))
    scaleMap = file.JudgeResolusion(path,list.get("solution"))
    for path,scale in scaleMap.items():
        Waifu2xExec.Waifu2x(waifu2xexec,path,output,scale)
