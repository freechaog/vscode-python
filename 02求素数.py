'''
    #sdf
'''

def sushua(num):
    """得到素数"""

    for i in range(1, num):
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            yield i


def sushub(num):
    "新解法"
    for i in range(2, int(num*0.5)+1):
        if num%i == 0:
            break
    else:
        return num

def sushuc(num):
    '''高效解法'''
    ps = [2]
    for i in range(3, num):
        for x in ps:
            if i % x == 0:      #可以加上根据平方根的判断
                break
        else:
            ps.append(i)
    return ps

L1 = sushuc(100000)
print(L1)


