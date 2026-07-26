def len(word):
    return len(word)

words = input("Enter words separated by space: ").split()

result = list(map(len, words))

print("Length of List:", result)