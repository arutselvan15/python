'''
:Author: Arutselvan Muthusamy
:Contact: arut.selvan15@gmail.com
'''
__updated__ = 'yyyy-MM-dd'

'''
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
'''
size = 6
rangoli = ord('a') - 1
length = size + (size - 1)
length = length + (length - 1)

draw = []
for i in range(1, size + 1):
    line = []
    topleft = rangoli + size

    for _ in range(i):
        line.append(chr(topleft))
        topleft -= 1
    
    topright = rangoli + size - (i - 2)
    for _ in range(i - 1):
        line.append(chr(topright))
        topright += 1
    draw.append('-'.join(line))

for i in range(size - 1, 0, -1):
    line = []
    bottomleft = rangoli + size

    for _ in range(i):
        line.append(chr(bottomleft))
        bottomleft -= 1

    bottomright = rangoli + size - (i - 2)
    for _ in range(i - 1):
        line.append(chr(bottomright))
        bottomright += 1
    draw.append('-'.join(line))

for i in draw:
    print(i.center(length, '-'))
