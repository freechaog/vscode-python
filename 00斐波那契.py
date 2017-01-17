x=0
y=0
for i in range(0,6):
    if i == 0:
        y = 1
    elif i == 1:
        x = 1
        y = 1
    else:
        temp = y
        y = x+temp
        x = temp
print(y)

'''用生成器来解决递归问题'''
def fib():
    a = 0
    b = 1
    while True:
        a, b = b,a+b
        yield a