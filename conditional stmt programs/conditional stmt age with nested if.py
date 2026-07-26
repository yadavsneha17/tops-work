age=int(input("enter a age "))
if age>=0 and age<=105:
    if age>=3 and age<=18:
        print("minor")
    elif age>=19 and age<=50:
        print("adult")
    elif age>=51 and age<=70:
        print("senior")
    elif age>0 and age<=2:
        print("infant")
else:
    print("  above super senior")
    