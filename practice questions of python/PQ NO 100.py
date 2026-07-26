def add_number(num):
    return num + num
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
value = int(input("Enter the number to add: "))
result = list(map(add_number, numbers))
print("Updated List:", result)