'''返回杨辉三角形指定行列的值'''
def yanghui(i, j):
    """杨辉三角"""
    if j+1 > i or j < 0 or i < 1:
        pass
    elif i == 1 or i == 2:
        return 1
    elif j == 0 or  i == (j+ 1):
        return 1
    else:
        return yanghui(i-1, j) + yanghui(i-1, j-1)

print(yanghui(6, 100))
