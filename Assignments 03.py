name = input("Enter any name: ")
value = name.lower()
total_vowels = 0
for i in value:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        total_vowels += 1

print(total_vowels)