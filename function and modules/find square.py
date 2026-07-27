def square(num):
    return num * num

def prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

num = int(input("Enter a number: "))

ans = square(num)
print("Square:", ans)

if prime(num):
    print("Prime")
else:
    print("Not Prime")

check_even_odd(num)