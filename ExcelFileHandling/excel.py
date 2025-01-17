# Date: 17 Jan 2025
# Python Class


import pandas as pd
from openpyxl import *


def create_excel():
    file_name = "students.xlsx"  # Fixed extension from xlxs to xlsx
    data = {
        "Name": ["John", "Alice", "Bob"],
        "Age": [25, 30, 22], 
        "City": ["New York", "London", "Paris"],
        "Email": ["john@example.com", "alice@example.com", "bob@example.com"]
    }
# Keys = Columns
    df = pd.DataFrame(data)
    print(df)
    df.to_excel(file_name, sheet_name = "student", index=False)
    print(f"Excel file '{file_name}' created successfully.")
    return df

def read_excel():
    file_name = "students.xlsx"  
    df = pd.read_excel(file_name)
    print(df)
    return df
    # table = tabulate(df, header='keys', showindex=False )
    
if __name__ == "__main__":
    # create_excel()
    read_excel()


# WAP to find the average marks of the students of five different subjects which name is starting from letter 'a'.
# WAP to Display the average marks and students names in console in tabular format.