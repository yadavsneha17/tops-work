age=int(input("enter age"))
match age:
    case m if 2<=m<=0:
        print("infant")
    case m if 3<=m<=18:
        print("minor")   
    case m if 50<=m<=19:
        print("adult")
    case m if 51<=m<=70:
        print("senior")
    case _:
        print("Above Super Senior")









       