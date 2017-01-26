'''
1 table ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
2 输入按三字节(24位)分组， 不足三字节补0
3 按6位分组， 转化为整数
4 整数作为table的索引
补0的字节用=表示
'''

def b64encode(data: bytes) -> str:
    table = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    encoded = bytearray()
    c = 0
    for x in range(3, len(data)+1, 3):
        print(data[c:x])
        i = int.from_bytes(data[c: x], 'big')
        for j in range(1, 5):
            encoded.append(table[i >> (24 - j*6) & 0x3f])
        c += 3
    r = len(data) - c
    if r > 0:
        i = int.from_bytes(data[c:], 'big') << (3-r) * 8
        for j in range(1, 5-(3-r)):
            encoded.append(table[i >> (24 - j*6) & 0x3f])
        for _ in range(3-r):
            encoded.append(int.from_bytes(b'=', 'big'))
    return encoded.decode()



'''
解码
'''

def b64decode(data:str) -> bytes:
    table = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    data = data.encode()

    decoded=bytearray()
    c = 0
    b=0
    for x in range(4,len(data)+1,4):
        for i,v in enumerate(data[b:x]):
            c+=table.index(v)<<24-(i+1)*6
        c=c<<24
        b+=4
    c=c>>24



    print(c.to_bytes(len(data)+1,'big'))


        

b64decode(b64encode(b'adcdef'))

