__author__ = 'kiryl_zayets'


def test1(param, list=[]):
    list.append(param)
    print(list)


def test2(param, list=list[:]):
    list =
    list.append(param)
    print(list)


def generate_smth():
    yield 3


for x in generate_smth():
    print(x)

test1(5)
test1(5)
test1(5)

test2(6)
test2(6)
