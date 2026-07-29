#Interesing pattern(row)

"""
1 14 15 28 29 
2 13 16 27 30 
3 12 17 26 31 
4 11 18 25 32 
5 10 19 24 33 
6 9 20 23 34 
7 8 21 22 35
"""

r = 7
c = 5

for i in range(r):
    for j in range(c):
        if j % 2 == 0:
            print(j * r + i + 1, end=" ")
        else:
            print((j + 1) * r - i, end=" ")
    print()