while True:
    print("\n1. Addition")
    print("\n2. Subtraction")
    print("\n3. Multiplication")
    print("\n4. Division ")
    print("\n5. Exit")
    choice=int(input("Enter choice "))
    match choice:
        
        case 1:  
            a = int(input("Enter first number: "))
            b= int(input("Enter second number: "))
            print("Result:",a+b)
        case 2:
            a= int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result:",a-b)
        case 3:
            a= int(input("Enter first number: "))
            b= int(input("Enter second number: "))
            print("Result:",a*b)
        case 4:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result:",a/b)
        case 5:
            print("Exit")
            break
        case _:
            print("Invalid choice!")
       