__author__ = 'kiryl_zayets'

def fibo(number):
    if number ==0: return 0
    if number ==1: return 1
    a=0
    b=1
    sum=0
    for i in range(0,number-1):
        sum=a+b
        a=b
        b=sum
        print (sum)
    return sum


fibo(13)