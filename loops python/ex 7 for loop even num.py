n = int(input("Enter how many even numbers: "))

sum = 0
for i in range(1, n + 1):
    sum += 2 * i

print("Sum:", sum)