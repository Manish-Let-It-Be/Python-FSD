# LAB : 2 
# 03 Dec, 24

# Baiscs


# Write a program to print the grades according to the percentage of marks.
# If percentage is > 80 then Grade - A; If 60 - 70 then Grade b, If it is < 60 then print Grade c


'''

m1 = int(input("Enter mark1: "))
m2 = int(input("Enter mark2: "))
m3 = int(input("Enter mark3: "))
m4 = int(input("Enter mark4: "))
m5 = int(input("Enter mark5: "))
Total = int(m1+m2+m3+m4+m5)
percentage = float((Total/500)*100)
print("Percentage : ", percentage , "%")
if(percentage >= 80):
    print("Grade A") 
elif(percentage >= 60 and percentage <= 70):
    print("Grade B")
elif(percentage <= 60):
    print("Grade C")
'''

# Write a program to print all the even numbers in reverse order and their sum in between a range
'''
num_range = int(input("Enter the range: "))
sum = 0
for i in range(num_range,0,-2):
    print("Even numbers :", i)
    sum += i
print("Sum : ", sum)

'''

#String iteration
'''
name = "Manish"
for i in name:
    print(i)
'''    
    
# Write a program to find the sum of digits of a given number by the user.

'''
number = input("Enter any number: ")
sum = 0
print("Digits of the number: ")
for i in number:
    print(i)
    sum += int(i)   
print("Sum of the digits: ",sum)
'''

# Write a program to take input numbers till the number is positive if the number is negative then terminate the input
# Also find the largest positive number given by the user


'''
largest_num = None
while True:
    num = float(input("Enter a number: "))
    if num < 0:
        break
    if largest_num is None or num > largest_num:
        largest_num = num
if largest_num is not None:
    print(f"The largest positive number entered is: {largest_num}")
else:
    print("No positive number was entered.")

'''


# PRACTICAL : 
# Set 1 => Practical 1.
# Write a program to convert Celcius to Fehrenheit and vice - versa after taking input from the user
'''
celcius = float(input("Enter Temperature in Celcius: "))
fehrenheit = float(9/5 * celcius + 32)
print("Temparature in Fehrenheit for ", celcius , "degree celcius is ", fehrenheit)

print("\n")

fehrenheit = float(input("Enter Temperature in fehrenheit: "))
celcius = float(5/9 * (fehrenheit - 32))
print("Temparature in celcius for ", fehrenheit , "degree fehrenheit is ", celcius)
'''




# PRACTICAL : 
# Set 1 => Practical 2.
# Write a program to calculate the area and perimeter of a rectangle

'''
lenght = float(input("Enter lenght: "))
breadth = float(input("Enter breadth: "))
area = float(lenght * breadth)
perimeter = float(2*(lenght+breadth))
print("Area of rectangle with lenght ", {lenght}, "and breadth ", {breadth}, "is : ", area, "unit square")
print("\n")
print("Perimeter of rectangle with lenght ", {lenght}, "and breadth ", {breadth}, "is : ", perimeter, "units")

'''


# Homework: Write a program to take input (numbers) separeted by coma and then find the target sum of two numbers without using SPLIT function.



# [CLASS] : 03 Dec, 24


# target = int(input("Enter target"))
# list = [1,2,3,4,5,6,7,8,9]
# for i in list:
#     for j in list:
#         if i+j==target:
#             print(i,",",j)




# list = ["Ram","adarsh","Raju"]
# # count = 0
# for i in list:
#     count = 0
#     for j in i:
#         if j == "a" or j == "e" or j == "i" or j == "o" or j == "u":
#             count += 1
#             if count == 2:
#                 print(i)
#                 # count =0




# list = "Hi there, this is a a demo text to to check the the deletion"
# st = list.split(" ")
# alt = []
# for data in st:
#     if data not in alt:
#         alt.append(data)
# print(alt)