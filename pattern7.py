#Numbers patterns

"""
1
2 9
3 8 10
4 7 11 14
5 6 12 13 15

"""
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i + 1):
        a=0
        for k in range(j):
            a = a + n - k
        if j % 2 == 0:
            print(a+i-j+1, end=" ")
        else:     
            print(a+n-i, end=" ")
    print()
