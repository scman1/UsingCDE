# import Document library from Chem Data Extractor
from chemdataextractor import Document
# import library for managing html requests
import requests

# The HTML document used in this example is the online version of:
# Silveri, F., Quesne, M. G., Roldan, A., De Leeuw, N. H., & Catlow, C. R. A. (2019). 
# Hydrogen adsorption on transition metal carbides: a DFT study. Physical Chemistry 
# Chemical Physics, 21(10), 5335-5343.

# the path for the html file is used directly
article_url = "https://pubs.rsc.org/ko/content/articlehtml/2019/cp/c8cp05975f"

# set request header
req_head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
# get the page content 
html_response = requests.get(article_url, headers = req_head)
#save the content as a temporary file in the local disk
f= open("temp.html","w+")
f.write(str(html_response.content))
f.close()

# open de temporary file and read in binary mode
f = open("temp.html", 'rb')

# create a document object from the file
doc = Document.from_file(f)


for element in doc.elements:
    print(element)

para = doc.elements[14]

print(para)
print("Sentences:", len(para.sentences))
print("Tokens:", para.tokens)
print("Tokens:", len(para.tokens))
print("Tokens:", len(para.tokens[0]))

#list of unique occurences
uniques=[]
for chement in doc.cems:
    #print(chement)
    if not chement.text in uniques:
        uniques.append(chement.text)

print("Unique entities:",len(uniques))

print(uniques)
serialised=doc.records.serialize()

print(len(serialised))

print(serialised)


