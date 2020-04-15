# import Document library from Chem Data Extractor
from chemdataextractor import Document
# import library for managing files
from pathlib import Path
import sys

def get_files_list(source_dir):
    i_counter = 0
    files_list = []
    for filepath in sorted(source_dir.glob('*.pdf')):
        i_counter += 1
        files_list.append(filepath)
    return files_list

def get_uniques(cde_doc):
    uniques={}
    for chement in cde_doc.cems:
        if not chement.text in uniques:
            uniques[chement.text] = 1
        else:
            uniques[chement.text] += 1
    return uniques

def get_max(uniques):
    max_val = 0
    max_lbl = ""
    for chement in uniques:
        if uniques[chement] > max_val:
            max_val = uniques[chement]
            max_lbl = chement.replace('\n',' ')
    return max_lbl, max_val

def cde_read_pdfs(argv, pdf_path = "./pdfs"):
    try:
        pdf_path = argv[0]
    except:
        print("missing arguments"+
              "\n -string pdf files path")
        return
    pdf_dir= Path(pdf_path)
    files_list = get_files_list(pdf_dir)
    print(files_list)
    for a_file in files_list:
        file_name = a_file.name
        pdf_f = open(a_file, 'rb')
        doc = Document.from_file(pdf_f)
        uniques = get_uniques(doc)
        max_lbl, max_val = get_max(uniques)       
        print(file_name, "Unique entities:", len(uniques), "Most common entity:", max_lbl, max_val)

if __name__ == "__main__":
   cde_read_pdfs(sys.argv[1:])

