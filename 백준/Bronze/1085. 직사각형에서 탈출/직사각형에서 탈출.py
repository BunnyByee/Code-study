x, y , w, h = map(int,input().split())

x1 = w - x; y1 = h - y

a = ( x if x <= x1 else x1)
b = ( y if y <= y1 else y1)

print( a if a <= b else b)