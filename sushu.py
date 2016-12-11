'''
    #sdf
'''

def sushu(num):
    """得到素数"""
    flag = False
    for i in range(1, num):
        for j in range(2, i+1):
            if j < i:
                if i%j == 0:
                    break
            elif j == i:
                flag = True
            else:
                break
        if flag is True:
            yield i
            flag = False
L1 = [i for i in sushu(1000)]
print(L1)
print(1235)

