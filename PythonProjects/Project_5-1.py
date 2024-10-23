# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

totat_h = 0
for height in student_heights:
    totat_h += height

total_s = 0
for  student in student_heights:
    total_s += 1

average = round(totat_h / total_s)
print(average)