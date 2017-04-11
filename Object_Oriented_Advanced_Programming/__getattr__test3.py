class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, attr):
        return Chain('%s/%s' % (self._path, attr))

    def __str__(self):
        return self._path

    def user(self, username):
        return Chain('GET /user/:%s' % username)


print Chain().user('michael')
