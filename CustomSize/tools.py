import getopt
import sys
def GetArg(argv):
    """
        通过 getopt模块 来识别参数demo,  http://blog.csdn.net/ouyang_peng/
    """

    username = ""
    password = ""
    execute="../waifu2x-ncnn-vulkan/waifu2x-ncnn-vulkan_waifu2xEX.exe"
    try:
        """
            options, args = getopt.getopt(args, shortopts, longopts=[])

            参数args：一般是sys.argv[1:]。过滤掉sys.argv[0]，它是执行脚本的名字，不算做命令行参数。
            参数shortopts：短格式分析串。例如："hp:i:"，h后面没有冒号，表示后面不带参数；p和i后面带有冒号，表示后面带参数。
            参数longopts：长格式分析串列表。例如：["help", "ip=", "port="]，help后面没有等号，表示后面不带参数；ip和port后面带冒号，表示后面带参数。

            返回值options是以元组为元素的列表，每个元组的形式为：(选项串, 附加参数)，如：('-i', '192.168.0.1')
            返回值args是个列表，其中的元素是那些不含'-'或'--'的参数。
        """
        opts, args = getopt.getopt(argv, "he:i:s:o:", ["help", "execute=", "input=","solution=","output="])
    except getopt.GetoptError:
        print('Error: test_arg.py -u <username> -p <password>')
        print('   or: test_arg.py --username=<username> --password=<password>')
        sys.exit(2)

    # 处理 返回值options是以元组为元素的列表。
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('main.py -e <waifu2x.exe> -i <inputpath> -o <output paht> -s <resolution>')
            sys.exit()
        elif opt in ("-e", "--execute"):
            execute = arg
        elif opt in ("-i", "--input"):
            input = arg
        elif opt in("-s","--solution"):
            solution=arg
        elif opt in("-o","--output"):
            output =arg

    result={"execute":execute,"input":input,"output":output,"solution":solution}
    return result

    # 打印 返回值args列表，即其中的元素是那些不含'-'或'--'的参数。
    # for i in range(0, len(args)):
    #     print('参数 %s 为：%s' % (i + 1, args[i]))

# if __name__ == "__main__":
#     print("helloworld")
#     ret= main(sys.argv[1:])
#     print(ret)