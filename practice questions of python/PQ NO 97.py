def square(num):
    return num * num

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

result = list(map(square, numbers))

print("Squared List:", result)