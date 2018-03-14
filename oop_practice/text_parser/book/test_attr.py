__author__ = 'kiryl_zayets'
import types

class AttrTest(object):

    def __init__(self, attr1='', wrapp=None):
        self.attr1 = attr1
        if wrapp:
            self.execute = types.MethodType(wrapp, self)
        self.wrapee = wrapp

    def __getattr__(self, item):
        if hasattr(self.wrapee, item):
            print('delegated to class')
            return self.wrapee.__dict__[item]
        else:
            self.wrapee.__dict__[item]= lambda x: print(x+1)
            return self.wrapee.__dict__[item]

    def execute(self):
        print('Aaaa')

    def ex(self):
        print('BBbb')


class AttrBase(object):
    def __init__(self):
        self.attr2 = 'attr2'

    def func2(self, *args):
        print('func2')


attrBase = AttrBase()

attr = AttrTest(attr1='attr2', wrapp=attrBase.func2)

attr.execute()

# attr.attr3(4)
# attr.attr3(7)