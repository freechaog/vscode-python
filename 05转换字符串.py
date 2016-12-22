"""字符串转数字"""

str1 = input("input a num:")
tmp = list(str1)
x = 0
if str1.count('.') > 0:
    for i, v in enumerate(list(str1.split('.'))):
        if i == 0:
            for j, y in v[::-1]:
                y = ord(v) - ord('0')
                y *= 10 ** j
                x += y
        else:
            for m, n in v[:]:
                y = ord(n) - ord('0')
                y *= 0.1 ** (m+1)
                x += y
    print('%d' % x)
else:
    tmp.reverse()
    for i, v in enumerate(tmp):
        y = ord(v) - ord('0')
        y *= 10 ** i
        x += y
    print('%d' % x)
