def box_area(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l

def slack_area(w, l, h):
    m = max(w,l,h)
    return int(w*l*h/m)

def ribbon_length(l, w, h):
    list = [l,w,h]
    list.remove(max(l,w,h))
    return list[0]*2+list[1]*2

def bow_legth(l, w, h):
    return l*w*h

lines = open('2015/Day2/input.txt').read().splitlines()
input = list()
for l in lines:
    input.append(l.split('x'))

#Part 1
total_area = 0
for i in input:
    l = int(i[0])
    w = int(i[1])
    h = int(i[2])
    total_area += box_area(l, w, h) + slack_area(l, w, h)

print('Total area: ' + str(total_area))

#Part 2
total_length = 0
for i in input:
    l = int(i[0])
    w = int(i[1])
    h = int(i[2])
    total_length += ribbon_length(l, w, h) + bow_legth(l, w, h)

print('Total ribbon length: ' + str(total_length))
