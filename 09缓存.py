'''
写一个函数缓存，允许过期，没有换出和清除
'''

import functools
import heapq

def fnCache(fn):
    def wrap(*args,**argkeywords):
        
        
       
        ret=dic.get((1,2),fn(*args,**argkeywords))
        return tuple(l1)
    return wrap

@fnCache
def add(x,y):
    print(x+y)
    
add(3,4)    