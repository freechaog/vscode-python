"""矩阵转置"""
def juzhenzhuanzhi(juz):
    """矩阵转置"""
    jzzz = []

    for i in range(0, juz.__len__()):
        for j in range(0, juz[i].__len__()):
            if jzzz.__len__() < j+1:
                jzzz.append([juz[i][j]])
            else:
                jzzz[j].append(juz[i][j])
    return jzzz

ZZ1 = juzhenzhuanzhi([(1, 2, 3), (4, 5, 6)])
print(ZZ1)
