def upper(word):
    return word.upper()

words = input("Enter a word : ").split()

result = list(map(upper, words))

print("Uppercase List:", result)