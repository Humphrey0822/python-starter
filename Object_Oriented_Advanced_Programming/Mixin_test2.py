# coding=utf-8
"""
Python自带的很多库也使用了Mixin。
举个例子，Python自带了TCPServer和UDPServer这两类网络服务，
而要同时服务多个用户就必须使用多进程或多线程模型，
这两种模型由ForkingMixin和ThreadingMixin提供。通过组合，我们就可以创造出合适的服务来。
"""
from SocketServer import TCPServer, UDPServer, ForkingMixIn, ThreadingMixIn


class MyTCPServer(TCPServer, ForkingMixIn):
    pass


class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
