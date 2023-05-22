# 如何在一个函数内部修改全局变量
a = 1
def fun1():
    global a
    a = 5
fun1()
print(a)
