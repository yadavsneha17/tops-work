student_data = {
    101: ["Kavyansh", "kavyansh@gmail.com", 20, [80, 90, 70]],
    102: ["Vivek", "vivek@gmail.com", 19, [70, 67, 80]],
    103: ["Varsha", "varsha@gmail.com", 20, [67, 89, 90]],
    104: ["sneha", "sneha@gmail.com", 20, [97, 89, 90]],
    105: ["megha", "megha@gmail.com", 20, [67, 29, 90]]
}
for id , details in student_data.items():
    name = details[0]
    marks = details[3]
    total = sum(marks)
    print(id, ":", total)
