#Reverse pattern program (row)

"""

15 
14 13
12 11 10
9 8 7 6
5 4 3 2 1

"""
n = 5
a = 0
for i in range(n):
    a = a + i
    b = n + a

for i in range(n):
    for j in range(i+1):
        print(format(b,"<3"), end=" ")
        b = b - 1
    print()