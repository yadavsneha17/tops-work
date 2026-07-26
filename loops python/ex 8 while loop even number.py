n = int(input("Enter how many even numbers: "))

sum = 0
i = 1

while i <= n:
    sum += 2 * i
    i += 1

print("Sum:", sum)