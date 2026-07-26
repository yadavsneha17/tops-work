marks=int(input("enter a marks: "))
match marks:
    case x if marks<=100 and marks>=80:print("A")
    case x if marks<=79 and marks>=60:print("B")
    case x if marks<=59 and marks>=45:print("C")
    case x if marks<=45 and marks>=0:print("D")
    case _:print("fail")
