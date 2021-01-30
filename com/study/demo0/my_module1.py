# def testA(a,b):
#     print(a+b)

__all__ = ["testA"]
def testA():
    print("testA")

def tesB():
    print("testB")


try:
    print(1/1)
    f = open("test.txt","r")
except Exception as msg:
    f = open("test.txt", "w")
else:
    print("没有异常")
finally:
    f.close()