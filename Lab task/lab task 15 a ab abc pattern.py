num=int(input("Enter no rows: "))

for i in range(1,num+1):
    for j in range(i):
        print(chr(97+j),end=" ")
    print()
