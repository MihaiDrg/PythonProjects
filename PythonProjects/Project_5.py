import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)

my_separator = ""
letters_pass = my_separator.join(letters[0:nr_letters])
numbers_pass = my_separator.join(numbers[0:nr_numbers])
symbols_pass = my_separator.join(symbols[0:nr_symbols])

password1 = letters_pass + numbers_pass + symbols_pass

password1_list = list(password1.strip(""))

random.shuffle(password1_list)

final_password = my_separator.join(password1_list)

print(final_password)


#CODE FROM COURSE


#password_list = []

#for char in range (1, nr_letters + 1):
#    password_list += random.choise(letters)

#for char in range (1, nr_numbers + 1):
#    password_list += random.choise(numbers)

#for char in range (1, nr_symbols + 1):
#    password_list += random.choise(symbols)

#random.shuffle(password_list)

#password = ""
#for char in password_list:
#    password += char

#print(password)
