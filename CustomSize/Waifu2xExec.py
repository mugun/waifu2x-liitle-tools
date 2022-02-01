import os
import shutil
def Waifu2x(execute,input,output,scale):
    filename = input.split("\\")[-1]
    outputpath=output+"\\"+filename
    if scale ==1 :
        shutil.copyfile(input,outputpath)
    else:
        command = execute+" -i "+input+" -s "+str(scale)+" -o "+outputpath+".png"
        # os.system(r"D:\waifu2x\Waifu2x-Extension-GUI-v3.83.35-beta-Win64\waifu2x-extension-gui\waifu2x-ncnn-vulkan\waifu2x-ncnn-vulkan_waifu2xEX.exe -h")
        print(command)
        os.system(command)

if __name__ == '__main__':
    Waifu2x(1,2,3,4)