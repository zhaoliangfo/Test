# fn2 = lambda: 100
# print(fn2)
# print(fn2())
#
# fn1 = lambda **kwargs: kwargs
# print(fn1(name='python', age=20))
#
# fn1 = lambda *args: args
# print(fn1(10, 20, 30))
#
#
# students = [
#  {'name': 'TOM', 'age': 20},
#  {'name': 'ROSE', 'age': 19},
#  {'name': 'Jack', 'age': 22} ]
# # 按name值升序排列
# students.sort(key=lambda x:x["name"])
# print(students)
#
# print(abs(-10))
# print(round(19.222))
#
#
# def pp(a,b,f):
#     t = f(a)+f(b)
#     return t
#
# print(pp(-9,-8.777,abs))
import time
from functools import reduce


def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print('call %s() in %fs' % (f.__name__, (t2-t1)))
        return r
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print(factorial(10))