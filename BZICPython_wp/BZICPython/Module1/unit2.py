# 注释：
# 注释是给程序猿看的，有时候也是给别人看的
# 解释器是不看注释的
# Python 里的注释是以 井号（ # ） 开头的
# 以井号开头的注释是单行注释
# 这是单行注释，如果切换到下一行时必须得重新打出一个井号，否则程序会报错
# hello  注释成功了的代码编辑器将默认设置为 深灰色 ，而没有成功的代码大部分都会变成 白色
# BZIClaw  # 这个代码没有注释掉，程序还是会看他的，然后就会…… 报错
print("HelloWorld!")
# print("HelloBZIClaw!")  # 这是一行注释，解释器不会将其执行 ！！！

# 注释的用处：
# 1. 调试程序
#    方法：单机要注释的那一行，按下快捷键 ctrl + / Mac 里是 cmd + /
# 2. 方便以后的调整
print("今天天气好晴朗")  # 用 双引号 或者 单引号 包裹起来的内容是字符串 str ，编辑器会自动将字符串的内容转换为黄色
# print(阳光明媚，照耀天空) # 这个内容不是黄色的，是白色的，说明有错误

# 现在看得懂的代码，不代表以后就能看懂
def numRange(number):  # 定义一个叫 numRange 的函数，并给他一个参数
    num = number  # 设置变量 num 等于参数的值
    for i in range(num):  # 循环 num 次数
        if i < num:  # 如果 i 小于 num
            i += 1  # i 加 1
        print(i)  # 输出 i
num = int(input("请输入循环次数："))  # 让用户输入次数
numRange(num)  # 调用循环函数

'''
我是
多行注释
多行注释大部分都是字符串一样的颜色
'''

"""
我也是
多行注释
黄色的
"""

# 添加注释
print("HelloWorld!")  # 在控制台里打印 HelloWorld!
