import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names_lenght = int(len(names)) - 1
random_number = random.randint(0, names_lenght)
random_name = names[random_number]
print(f"{random_name} is going to buy the meal today!")
