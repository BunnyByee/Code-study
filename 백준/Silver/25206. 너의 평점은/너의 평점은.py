table = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 
         'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}

name = ''
credit = ''
grade = ''
hap = 0.0
c_hap = 0.0

for _ in range(20):
    name, credit, grade = input().split()

    # P면 넘어감
    if grade == 'P':
        continue
    hap += float(credit)*table[grade]
    c_hap += float(credit)

print(hap/c_hap)