# LAB : 4
# 17 Dec, 24


# SET 2 => Practical 1
# School Management System having Student Teacher Courses

import random
import string
import os
from tabulate import tabulate
from openpyxl import Workbook, load_workbook

database = "school.xlsx"

class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []
        self.programs = []
