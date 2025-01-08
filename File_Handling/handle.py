# # def write_in_file():
# #     try:
# #         with open("test.txt", "w") as file:
# #             file.write("Hello, world! This file is created by write_in_file() function")
# #         print("File written successfully.")
# #     except Exception as e:
# #         print(e.args)



# def write_in_file_sir():
#     try:
#         file_name="demo.txt"
#         file=open(file_name, 'w')
#         file.write("Hi this created by write_in_file_sir() function\n")
#         file.close()
#     except Exception as e:
#         print(e.args)

# def append_in_file():
#     try:
#         file_name= "demo.txt"
#         file=open(file_name, 'a')
#         data=["This is first line\n"
#               "This is second line\n"
#               "This is third line\n"]
#         file.writelines(data)
#         file.close
#     except Exception as e:
#         print(e.args)


# def read_from_file():
#     try:
#         file_name="demo.txt"
#         file=open(file_name, 'r')
#         data=file.read()
#         print(data)


#     except Exception as e:
#         print(e.args)     




# if __name__ == '__main__':
#     # write_in_file()
#     write_in_file_sir()
#     append_in_file()
#     read_from_file()



# # WAP to print all the usernames of a file which starts with "a" where create a file to prompt the user to enter n number of usernames.

# def take_input():
#     num = input("Enter number of Usernames to store: ")
#     list=[]

#     for i in num:
#         usernames = input("Enter Username: ")
#         list.append(usernames)

#     def append_in_file():
#             try:
#                 file_name="username.txt"
#                 file=open(file_name, 'a')
#                 data=usernames
#                 file.writelines(data)
#                 file.close()

#             except Exception as e:
#                 print(e.args)

#     def initial_with_a():
#          file_name="username.txt"
#          file=open(file_name, 'r')
#          data=file.read()
#          temp = data.split()
#          if (temp == 'a'):
#               return temp

# if __name__=='__main__':
#     take_input()


# Sir's code
# def check():
#     file_name="name.txt"
#     num_of_names=int(input("Enter the number of names :"))
#     file=file_name
#     file=open(file_name, 'a')
#     for i in range (1, num_of_names):
#         file.write(input(("Enter the names:") + "\n"))
#     file.close()

#     file=open(file_name, 'r')
#     data=file.readlines()
#     for name in data:
#         if name.lower().startswith('a'):
#             print(name)



# if __name__ == '__main__':
#     check()




# New 
# def write_usernames_to_file(filename, n):
#     with open(filename, 'w') as file:
#         for _ in range(n):
#             username = input("Enter a username: ")
#             file.write(username + '\n')

# def print_usernames_starting_with_a(filename):
#     with open(filename, 'r') as file:
#         usernames = file.readlines()
#         for username in usernames:
#             if username.strip().lower().startswith('a'):
#                 print(username.strip())

# def main():
#     filename = 'usernames.txt'
#     n = int(input("Enter the number of usernames you want to input: "))
#     write_usernames_to_file(filename, n)
#     print("\nUsernames starting with 'a':")
#     print_usernames_starting_with_a(filename)

# if __name__ == "__main__":
#     main()


# WAP to count the number of words in a gievn file.
# Write function for many below programs
# def write_to_file(filename):
#     try: 
#         with open(filename, 'w') as file:
#             data = input("Enter data to write to the file: ")
#             file.writelines(data)
#     except Exception as e:
#         print(e.args)


# def count_words_in_file(filename):  
#     try:

#         with open(filename, 'r') as file:
#             data = file.read()
#             words = data.split()
#             characters = len(data)
#             return len(words), characters
#     except Exception as e:
#         print(e.args)


# if __name__ == "__main__":
#     filename = "data.txt"
#     write_to_file(filename)
#     words = count_words_in_file(filename)
#     print(f"Number of words & characters in the file: {words}")


# WAP to count the number of lines in a file.

# def count_lines(filename):
#     try:
#         with open(filename, 'r') as file:
#             lines = file.readlines()
#             return len(lines)
#     except Exception as e:
#         print(e.args)


# if __name__ == "__main__":
#     filename = "data.txt"
#     write_to_file(filename)
#     lines = count_lines(filename)
#     print(f"Number of lines in the file: {lines}")


# WAP to find a specific word in a file.

# def find(filename, word):
#     try:
#         with open(filename, 'r') as file:
#             data = file.read()
#             if word in data:
#                 print("found")
#             else:
#                 print("not found")
#     except Exception as e:
#         print(e.args)

# if __name__ == "__main__":
#     filename = "data.txt"
#     write_to_file(filename)
#     word = input("Enter the word to search: ")
#     found = find(filename, word)
#     print(f"Word '{word}'")


#WAP to copy the content of one file to another file.

# def copy_file(source, destination):
#     try:
#         with open(source, 'r') as source, open(destination, 'w') as destination:
#             data = source.read()
#             destination.write(data)
#     except Exception as e:
#         print(e.args)

# if __name__ == "__main__":
#     source = "source.txt"
#     destination = "destination.txt"
#     write_to_file(source)
#     copy_file(source, destination)
#     print("Copied successfully.")









####################################################################################################################################################

# HOMEWORK : DATE : 07 Jan, 2025

####################################################################################################################################################

#1 WAP to find the average of all the numbers stored in a file.

#2 WAP to remove duplicate lines from a file.

#3 WAP to replace the found word with a new word.

#4 WAP to remove blank lines from the file.

#5 WAP to find the count of vowels and consonants in a given file.


