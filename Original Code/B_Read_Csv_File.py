""" 
Continue: After Part 1 
Mod Date: 061122, Sunday
Watch Date: 071122, Monday, 07.15 pm
21-1 Module Introduction and previous module recap
"""
import csv 

lst = []
with open('./data/My_Csv_data.csv', 'r') as file:
        lines = csv.reader(file)
        header = next(lines)  # this will remmove the header file if we need to skip the header file in csv 
        for line in lines:
                if 'Alam' in line[1]:
                        print(line)
                lst.append(line)

print(lst)
