employee = {
    101: ["sneha", "sneha@gmail.com", 80000, "data science"],
    102: ["Varsha", "varsha@gmail.com", 70000, "data science"],
    103: ["umang", "umang@gmail.com", 60000, "software engineer"],
    104: ["prince", "prince@gmail.com", 50000, "software engineer"],
    105: ["ram", "ram@gmail.com", 45000, "cybersecurity"]
}
while True:
    print("\nMenu:")
    print("1. Add Employee")
    print("2. View Employee - department wise")
    print("3. All Employees")
    print("4. Delete Employee")
    print("5. Calculate Salary")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            emp_id = int(input("Enter employee id: "))
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            salary = int(input("Enter Salary: "))
            department = input("Enter Department: ")
            employee[emp_id] = [name, email, salary, department]
            print("Employee added successfully....")
        case "2":
            dept = input("Enter Department to view: ")
            print(f"\nEmployees in {dept} Department:")
            for emp_id, details in employee.items():
                print(emp_id, "--->", details)
        case "3":
            print("\nAll Employees:")
            for emp_id, details in employee.items():
                print(emp_id, "--->", details)
        case "4":
            emp_id = int(input("Enter Employee id to delete: "))
            if emp_id in employee:
                del employee[emp_id]
                print("Employee deleted successfully...")
            else:
                print("Employee not found....")
        case "5":
            total = sum(details[2] for details in employee.values())
            print("Total Salary of all employees:", total)
        case "6":
            print("Exiting program...")
            break   
        case _:
            print("Invalid choice Please try again....")


    