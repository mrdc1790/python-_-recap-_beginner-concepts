import zipfile
import shutil
import re
import os
import pathlib

filename = "C:\\Users\\padam\\OneDrive\\Documents\\PYTHON - learning - projects\\tutorials\\recaps\\newModules -easy02\\unzip_me_for_instructions.zip"
extract_directory = "C:\\Users\\padam\\OneDrive\\Documents\\PYTHON - learning - projects\\tutorials\\recaps\\newModules -easy02"
archive_format = 'zip'

shutil.unpack_archive(filename, extract_directory, archive_format)

filenumbers = ["One","Two","Three","Four","Five"]

workFolder = "C:\\Users\\padam\\OneDrive\\Documents\\PYTHON - learning - projects\\tutorials\\recaps\\newModules -easy02\\extracted_content"

for i in range(len(filenumbers)):
    os.chdir(workFolder +"\\"+ filenumbers[i])
    x = len([name for name in os.listdir(workFolder +"\\"+ filenumbers[i]) if os.path.isfile(name)])
    y = ""
    for i in range(len(filenumbers)):
      for path in pathlib.Path(workFolder +"\\"+ filenumbers[i]).iterdir():
            if path.is_file():
                current_file = open(path, 'r')
                for match1 in re.findall(r'\d{3}-\d{3}-\d{4}', current_file.read()):
                    print(current_file.name)
                    y = match1
                    print(match1)
                current_file.close()
    if y is not None:
        break