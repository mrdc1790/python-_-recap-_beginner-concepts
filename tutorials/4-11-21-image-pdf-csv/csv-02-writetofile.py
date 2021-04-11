import csv

# file_to_output = open('to_save_file.csv', mode='w', newline='') ## overwrites files w same name
# csv_writer = csv.writer(file_to_output, delimiter=',')
# csv_writer.writerow(['a','b','c'])
# csv_writer.writerows([['1','2','3'],['4','5','6']])
# file_to_output.close()

f = open('C:\\Users\\polla\\OneDrive\\Documents\\PYTHON - learning - projects\\tutorials\\4-11-21-image-pdf-csv.to_save_file.csv', mode='w',newline='')
hi = csv.writer(f)
hi.writerow(['f','d','s'])
f.close()