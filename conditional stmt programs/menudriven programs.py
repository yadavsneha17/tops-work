while True:
    print("\n1. Addition")
    print("\n2.subtraction")
    print("\n3.multiplication")
    print("\n4.division")
    print("\n5.exit")
    choice=int(input("Enter choice "))
    match choice:
        
        case 1:  
            a = int(input("Enter first number: "))
            b= int(input("Enter second number: "))
            print("Result:",a+b)
        case 2:
            a = int(input("enter a number: "))
            b = int(input("enter a number: "))
            print("Result:",a-b)
        case 3:
            a = int(input("enter a number"))
            b = int(input("enter a number: "))
            print("Result:",a*b)
        case 4:
            a = int(input("enter a number: "))
            b = int(input("enter a number: "))
            print("Result:",a/b)
        case 5:
            print("Exit")
            break
        case _:
            print("Invalid choice!")
       


