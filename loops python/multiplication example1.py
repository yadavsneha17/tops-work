num=int(input("enter a number "))
if num%2==0:
    for i in range(1,11):
        print(f"{num} * {i} ={num*i}")
    else:
        print("multiplication not perform")