import csv
import PyPDF2
import re

data = open('C:\\Users\\polla\\OneDrive\\Documents\\SCHOOL\\Python Tutorials-Practice\\Complete-Python-3-Bootcamp-master\\15-PDFs-and-Spreadsheets\Exercise_Files\\find_the_link.csv',encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
link_str = ''
for row_num,data in enumerate(data_lines):
    link_str+= data[row_num]
print(link_str)

f = open('C:\\Users\\polla\\OneDrive\\Documents\\SCHOOL\\Python Tutorials-Practice\\Complete-Python-3-Bootcamp-master\\15-PDFs-and-Spreadsheets\Exercise_Files\\Find_the_Phone_Number.pdf',mode='rb')
pdf = PyPDF2.PdfFileReader(f)
print(pdf.numPages)
pattern = r'\d{3}.\d{3}.\d{4}'
all_text = ''
for n in range(pdf.numPages):
    page = pdf.getPage(n)
    page_text = page.extractText()
    all_text = all_text+" "+page_text

print(re.search(pattern, all_text))
for match in re.finditer(pattern, all_text):
    print(match)
    ## it shows the span, so print out that range!
print(all_text[41790:41808+12])