import PyPDF2
import re
import sys
from pathlib import Path

cwd = Path.cwd()
name_folder = ""
location_outfile = ""
target_dir = cwd / name_folder

iteration = 0
for filename in target_dir.iterdir():
    
    pattern = re.compile(r"\d{4,10}\s*[.]*\d{2,10}\s*[.]*\d{3,10}")

    with open(filename, "rb") as file:
        pdf = PyPDF2.PdfFileReader(file)
        print(filename.name)
        match_iteration = 0
        for page_num in range(pdf.numPages):
            page = pdf.getPage(page_num)
            text = page.extractText()

            matches = pattern.finditer(text)

            for match in matches:
                pot_acc_no = match[0]
                print(pot_acc_no)
                if match_iteration == 0:
                    match_string = str(pot_acc_no)
                else:
                    match_string = match_string + "\t" + str(pot_acc_no)

                match_iteration+=1

    
    full_string = str(filename.name) + "\t" + match_string

    if iteration == 0:
        new_string = full_string
    else:
        new_string = new_string + "\n" + full_string
    
    iteration +=1

with open (location_outfile, "w") as f:
    f.write(new_string)

    

       
        

