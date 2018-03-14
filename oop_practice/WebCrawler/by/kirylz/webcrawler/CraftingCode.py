__author__ = 'kiryl_zayets'

def isPolyndrom(string):
    reversedString = ""
    for s in string:
        reversedString = s + reversedString
    return reversedString == string


def isPolyndrom2(string):
    flag = True
    for i in range(len(string)//2):
        if string[i]!=string[len(string)-i-1]:
            flag=False
    return flag



print(isPolyndrom2('ololo'))