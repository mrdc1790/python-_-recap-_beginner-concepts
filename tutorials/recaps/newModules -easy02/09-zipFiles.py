import zipfile
import shutil

f = open('fileone.txt','w+')
f.write('ONE FILE')
f.close()

f = open('filetwo.txt','w+')
f.write('TWO FILE')
f.close()

comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall('extracted_content')

dir_to_zip = 'C:\\Users\\polla\\OneDrive\\Documents\\PYTHON - learning - projects\\tutorials\\recaps\\newModules -easy02'
output_filename = 'example'
shutil.make_archive(output_filename, 'zip',dir_to_zip)
## ^^ this last example is important: you can zip an entire directory thru python

shutil.unpack_archive('example.zip', 'final_unzip', 'zip')
## ^^ this example unpacks said zip file into the current working directory; read documentation