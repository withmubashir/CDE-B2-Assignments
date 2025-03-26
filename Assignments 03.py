# Question 1

# name = input("Enter any name: ")
# value = name.lower()
# total_vowels = 0
# for i in value:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#         total_vowels += 1

# print(total_vowels)

# # Question 2

# input = input("Enter any string: ")

# uppercase = 0
# lowercase = 0
# digits = 0
# whitespace = 0

# for letter in input:
#     if letter.isupper():
#         uppercase += 1
#     elif letter.islower():
#         lowercase += 1
#     elif letter.isdigit():
#         digits += 1
#     elif letter.isspace():
#         whitespace += 1

# print(uppercase)
# print(lowercase)
# print(digits)
# print(whitespace)

# Question 3

revers = input("Enter any Input: ")
new_revers = revers[-1] + revers[1:-1] + revers[0]
print(new_revers)