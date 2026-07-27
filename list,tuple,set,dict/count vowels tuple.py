names = ("Sneha", "Varsha", "Prince", "Umang", "Ram")

for name in names:
    count = 0
    
    for ch in name.lower():
        if ch in "aeiou":
            count += 1
    print(name, ":", count)