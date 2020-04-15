from chemdataextractor import Document

doc = Document('UV-vis spectrum of 5,10,15,20-Tetra(4-carboxyphenyl)porphyrin in Tetrahydrofuran (THF).')

print('Chemical entities(cems):\n',doc.cems)

print('abbreviation definitions:\n',doc.abbreviation_definitions)

print('Records:\n',doc.records)

print('Record 0:\n', doc.records[0].serialize())

print('Record 1:\n', doc.records[1].serialize())

filepath = "pdfs/c8cp05975f.pdf"

f = open(filepath, 'rb')

doc = Document.from_file(f)#, readers=[PdfReader()])

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

serialised=doc.records.serialize()

print(len(serialised))
