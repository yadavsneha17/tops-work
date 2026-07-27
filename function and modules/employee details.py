def employee_details(*args):
    company_name = "GOOGLE"

    print("Company Name :", company_name)
    print("Employee_Name:",)
    print("Department   :", args[1])
    print("Salary       :", args[2])
    print("Email        :", args[3])


# Function Cal
employee_details("SNEHA", "IT", 50000, "rahul@gmail.com")

print()

employee_details("Priya", "HR", 45000, "priya@gmail.com")