marks=int(input("enter a marks"))
if marks>0:

    if marks>=80 and marks<=100:
        print("grade A")
    elif marks>=60 and marks<=79:
        print("grade b")
    elif marks>=45 and marks<=59:
        print("grade c")
    elif marks < 45 and marks >= 0:
        print("Grade D")
else:
    print("Invalid marks")

    



