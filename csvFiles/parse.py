import csv
from tabulate import tabulate

# with open('new_names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t')

#     # next(csv_reader) # Skips the first line

#     # with open('new_names.csv', 'w') as new_file:
#     #     csv_writer = csv.writer(new_file, delimiter='\t')

#     #     for line in csv_reader:
#     #         csv_writer.writerow(line)

#     for line in csv_reader:
#         print(line)
#         # print(line[0])  # Can print specific coloumns with the help of index



# with open('new_names.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     for line in csv_reader:
#         print(line)
    
# with open('new_names.csv', 'w') as new_file:
#     fieldnames = ['first_name', 'last_name', 'email']

#     csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

#     csv_writer.writeheader()

#     for line in csv_reader:
#         csv_writer.writerow(line)


# SIR Code || Date : 17 Jan 2025  || Python Class
def create():
    file_name = "students.csv"
    with open(file_name, 'w', newline="") as new_file:
        writer = csv.writer(new_file)
        header = ['first_name', 'last_name', 'email']
        data = [
            ['Manish', 'Sharma', 'XXXXXXXXXXXXXXXX'],
            ['Rahul', 'Sharma', 'XXXXXXXXXXXXXXXX'],
            ['Shreyas', 'Sharma', 'XXXXXXXXXXXXXXXX'],
        ]
        writer.writerow(header)
        writer.writerows(data)
        print("File created")

def read():
    file_name = "students.csv"
    with open(file_name, 'r') as new_file:
        reader = csv.reader(new_file)
        for line in reader:
            print(line)

def read_with_tabulate():
    file_name = "students.csv"
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        headers = data[0] 
        rows = data[1:]   
        
        table = tabulate(rows, headers=headers, tablefmt='grid')
        # table = tabulate(data, tablefmt='grid')
        print(table)

if __name__ == "__main__":
    create()
    # read()
    read_with_tabulate()