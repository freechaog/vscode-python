from collections import namedtuple

MapItem = namedtuple('MapItem', ['name', 'convert'])

mapping = [
    MapItem('lenth', int),

]

print(mapping[0].convert('123'))

mapdict={
    'a':123

}



