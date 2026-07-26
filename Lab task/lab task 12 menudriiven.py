while True:
    print("\n1. Factorial")
    print("\n2. Count Digit")
    print("\n3. Sum of Digits")
    print("\n4. Prime Number or not a prime number  ")
    print("\n5. Exit")
    choice=int(input("Enter choice "))
    match choice:
        case 1:
            num=int(input("Enter number "))
            fact=1
            for i in range(1,num+1):
                fact*=i
            print(f"Factorail of {num} is {fact}")
        case 2:
            num=int(input("Enter number "))
            count=0
            num1=num
            while num!=0:
                rem=num%10
                count+=1
                num=num//10
            print(f"{num1} contains {count} digits")
        case 3:
            num=int(input("enter aa number "))
            count=0
            num1=num
            while num!=0:
                rem = num % 10
                print("rem=== ",rem)
                count+=1
                num=num//10
                print(f"{num1} contains {count} digits")
        case 4:
            n =int(input("enter a number: "))
            if n> 1:
                for i in range(2, n):
                    if n % i==0:
                        print("not a  prime number ")
                        break
                else:
                        print("it was a prime number ")
            else:
                    print("not a  prime number")
        case 5:
            break
        case _:
            print("Invalid Choice")
