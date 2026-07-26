n =int(input("enter a number: "))
if n> 1:
    for i in range(2,n):
        if n % i==0:
            print("not a prime number ")
            break
    else:
        print("it was a prime number ")
else:
    print("not a  prime number")
