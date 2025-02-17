list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()

for i in list:
    s = s.replace(i,"_")

print(len(s))