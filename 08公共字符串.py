def subC(orglist,lstB):
    def subL(orglist,lstB, sublen = 1, index = 0, substr=None):
        for i in range(index , len(orglist)):
            sl1=slice(i,i+sublen)
            if(lstB[sl1] in  orglist and  i+sublen<len(lstB)+1):
                rsl = subL(orglist,lstB,sublen+1,i,lstB[sl1])
                return rsl             
        else:
             return substr

    return subL(orglist,lstB)
        
 
    

c=subC('abcdefghaaaaaaaaaaa','aaaaaaa')


print(c)

'''使用矩阵计算，最长对角线即为最长公共字符串

s1='aaabc'
s2='abc'

1 0 0
1 0 0
1 0 0
0 1 0
0 0 1
'''
def lcs(s1,s2):
    dp = []
    ml = 0
    mi = 0
    for i,m in enumerate(s1):
        dp.append([])
        for j,n in enumerate(s2):
            if m == n:
                if i>0 and j>0:
                    dp[i].append(dp[i-1][j-1]+1)
                else:
                    dp[i].append(1)
                if dp[i][j]>ml:
                    ml = dp[i][j]
                    mi = i+1-ml
            else:
                dp[i].append(0)
    return mi,ml

s=lcs('abc','gabcd')

print(s)




