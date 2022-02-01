import os
from PIL import Image
import math
def filePath(path):
    list=[]
    for filepath,dirnames,filenames in os.walk(path):
        for filename in filenames:
            list.append(os.path.join(filepath,filename))
    return list

def JudgeResolusion(list,solution):
    targetWidth = int(solution.split("*")[0])
    targetHeigh = int(solution.split("*")[1])
    tuple={}
    for i in list :
        img = Image.open(i)
        # imgSize = img.size  # 大小/尺寸
        w = img.width  # 图片的宽
        h = img.height  # 图片的高
        img.close();
        if w<targetWidth and h<targetHeigh:
            scale=max(math.ceil(targetHeigh/h),math.ceil(targetWidth/w))
            if scale ==2:
                scale=2
            elif scale >2 and scale <=4:
                scale =4
            elif scale>4 and scale<=8:
                scale=8
            elif scale>8 and scale<=16:
                scale=16
            else :
                scale=32
            temp={i:scale}
            tuple.update(temp)
        else:
            temp = {i: 1}
            tuple.update(temp)
    return tuple




# if __name__ == "__main__":
#     list=filePath(r"C:\Users\fsxn2\Downloads\光崎的插图・漫画 - pixiv")
#     aaa=JudgeResolusion(list,"1920*1080")
#     for k,v in aaa.items():
#         print(k+" "+str(v))