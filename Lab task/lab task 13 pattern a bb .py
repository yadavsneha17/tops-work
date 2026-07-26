num=int(input("Enter no "))

for i in range(num):
    for j in range(i+1):
        print(chr(65+i),end=" ")
    print()