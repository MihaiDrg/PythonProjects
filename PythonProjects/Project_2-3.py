# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_age = 90-int(age)
days = int(new_age)*365
weeks = int(new_age)*52
months = int(new_age)*12

print(f"You have {days} days, {weeks} weeks, and {months} months left. ")