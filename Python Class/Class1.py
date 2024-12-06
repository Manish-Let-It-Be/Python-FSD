# [CLASS] : 03 Dec, 24

# Q. Print two elemets from the list that sums to given target. 
# target = int(input("Enter target"))
# list = [1,2,3,4,5,6,7,8,9]
# for i in list:
#     for j in list:
#         if i+j==target:
#             print(i,",",j)



# Q. Print the name if it contains any two vowels.
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



# Q. Delete duplicate words from a given sentence
# list = "Hi there, this is a a demo text to to check the the deletion"
# splitSen = list.split(" ")
# uniqueSen = []
# for data in splitSen:
#     if data not in uniqueSen:
#         uniqueSen.append(data)
# print(uniqueSen)




# Q. Given, numbers[1234, 226, 349, 28] ; expected output1 = [4, 3, 3, 2] & output2 = [10, 10, 16, 10] using Comprehension

# numbers = [1234, 226, 349, 28]
# list = [len(str(val)) for val in numbers  ]
# print(list)


# dict = {
#     1 : 25,
#     2 : 50,
#     3 : 130,
#     4 : 150
# }

# for key in dict.items(): 
    # print(key[0]) #Prints the keys 
    
    # print(key[1])  #Print the values

    # print(key)  # Print key value pair



'''
Q. WAP to calculate the marks percentage of student and print in this format: 
{
    "Student1" : 89%
    "Student2" : 70%

}

 Calculate percentage for those students whose name starts with letter "A" and are living in "Vadodara"
'''

data = [{
    "name" : "manish",
    "marks" : [10,20,30,40,50],
    "location" : "Vadodara"

},
{
    "name" : "adarsh",
    "marks" : [99,100,100,98,99],
    "location" : "Vadodara"
}
]

