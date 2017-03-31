# coding=utf-8
"""
    一层装饰器的函数带参数
"""


class User:
    def __init__(self, username, is_allowed_login):
        self.username = username
        self.is_allowed_login = is_allowed_login


u = User("humphrey", False)

aa = lambda user: user.is_allowed_login

# print aa
# print aa(u)


def user_pass_test(is_allowed_login):
    def handle_fun(func):
        def handle_args(user):
            if not is_allowed_login(user):
                print "user can't vote, return"
                return
            else:
                print "user can vote"
            func(user)
        return handle_args
    return handle_fun


@user_pass_test(lambda u: u.is_allowed_login)
def vote(u):
    print "%s vote is %s" % (u.username, u.is_allowed_login)


vote(u)
