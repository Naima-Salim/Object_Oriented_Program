from multiprocessing.connection import answer_challenge

from httplib2 import FailedToDecompressContent


def add(a,b):
    answer=a+b
    return answer
def subtract(a,b):
    answer=a-b
    return answer
def multiply(a,b):
    answer=a*b
    return answer
def division(a,b):
    answer=a/b
    return answer
def modulus(a,b):
    answer=a%b
    return answer
def exponent(a,b):
    answer=a**b
    return answer
def integer_division(a,b):
    answer=a//b
    return answer
def square(a,b):
    answer=a*b
    return answer
def cube(a,b,c):
    answer=a*b*c
    return answer


def factorial(num):
    factor=1
    for a in range(1, num + 1):
        factor*= a
    return factor

   


