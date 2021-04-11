import pandas as pd
import csv

data = open('C:\\Users\\polla\\anaconda3\\AComplete-Python-3-Bootcamp-master\\15-PDFs-and-Spreadsheets\\example.csv',encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
print(data_lines[0]) ## id[0], first_name[1], last_name[2], email[3], gender[4], ip_address[5], city[6] <--- all in 2d array

## if you wanna grab just emails from users:
all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])
for i in all_emails:
    print(i)
print('\n\n')
## if you wanna grab full names from users (full + last):
full_names = []
for line in data_lines[1:15]:
    full_names.append(line[1] + " " + line[2])
for i in full_names:
    print(i)