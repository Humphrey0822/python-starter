# coding=utf-8
import os

print os.name  # 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

# print os.uname()  # 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的

# 环境变量
print os.environ  # 操作系统中定义的环境变量
print os.getenv('PATH')  # 获取某个环境变量的值，可以调用os.getenv()函数

# 操作文件和目录
# 查看当前目录的绝对
print os.path.abspath('.')

# 在某个目录下创建一个新目录
# 首先把新目录的完整路径表示出来：
# testdir_path =  os.path.join('D:\\PythonDevelop\\PycharmProjects\\python-starter\\file_io', 'testdir')
testdir_path = 'testdir'
# 然后创建一个目录
os.mkdir(testdir_path)
# 删掉一个目录：
# os.rmdir(testdir_path)

# 拆分路径:这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print os.path.split('D:\\PythonDevelop\\PycharmProjects\\python-starter\\file_io\\file.txt')
# os.path.splitext()可以直接让你得到文件扩展名
print os.path.splitext('D:\\PythonDevelop\\PycharmProjects\\python-starter\\file_io\\file.txt')
"""
这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
"""