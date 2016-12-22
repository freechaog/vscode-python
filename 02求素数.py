'''
    #sdf
'''

def sushu(num):
    """得到素数"""

    for i in range(1, num):
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            yield i


def sushus(num):
    "新解法"
    for i in range(2, int(num*0.5)+1):
        if num%i == 0:
            break
    else:
        return num

L1 = [i for i in sushu(20)]
print(L1)
print(sushu1(3))

