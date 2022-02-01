# waifu2x小工具
目前实现了可以指定目录后，根据目录内的图片的像素大小，自定义是否放大与自动设定放大倍数

调用方法如下  
CustomSize包下  
main.py -e D:\waifu2x\Waifu2x-Extension-GUI-v3.83.35-beta-Win64\waifu2x-extension-gui\waifu2x-ncnn-vulkan\waifu2x-ncnn-vulkan_waifu2xEX.exe -i C:\Users\fsxn2\Downloads\hikazaki -s 1920*1080 -o G:\temp  
参数含义如下:  
-e 指定waifu2x的运行exe文件 不指定则为默认根目录下的../waifu2x-ncnn-vulkan/waifu2x-ncnn-vulkan_waifu2xEX.exe  
-i 指定输入的图片的文件夹  
-s 指定放大的目标的分辨率 目前不允许自由拉伸，这个分辨率模式只是用来判断宽和高以确定放大比例而已  
-o 输出目录  