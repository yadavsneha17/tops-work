student_data= {
    101:["sneha","sneha@gmail.com",20,120],
    102:["varsha","varsha@gmail.com",24,130],
    103:["priya","priya@gmail.com",20,110],
}
roll_no=int(input("enter a roll no :" ))
if roll_no in student_data.keys():
    print(student_data[102])
else:
    print(f"{roll_no} doesn't exist")
for i,j in student_data.items():
    print(i)
    for i1 in j:
        print("\t",i1)
# fetch email address of students 
for j in student_data.values():
    print(j[1])
