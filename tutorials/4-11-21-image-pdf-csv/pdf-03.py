import PyPDF2

f = open('C:\\Users\\polla\\OneDrive\\Documents\\SCHOOL\\Python Tutorials-Practice\\Complete-Python-3-Bootcamp-master\\15-PDFs-and-Spreadsheets\\Working_Business_Proposal.pdf','rb')
pages_of_text = []
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)
page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
## can then use regex to look for passages

for i in range(5):
    pages_of_text.append((pdf_reader.getPage(i).extractText()))
    print(pages_of_text[i])