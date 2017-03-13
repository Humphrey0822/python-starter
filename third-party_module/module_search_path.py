# coding=utf-8
import sys

print sys.path
# 直接修改sys.path，添加要搜索的目录
# 这种方法是在运行时修改，运行结束后失效
sys.path.append('/User/humphrey/my_py_script')