#écrit par Joshua Vachon

import PyPDF4
e1 = []
e2 = []
x = 0
livre = ['1.couvertureLivre.pdf','2.table.pdf','3.Intro.pdf','4. Sphoungata.pdf','5.Brouet de canelle.pdf','6.boereksdocx.pdf', '7.fricassee.pdf', '8.Kougelhopf_V2.pdf', '9.pelmenis2.pdf',  '10.pate chinois.pdf', '11.banane.pdf', '12.bolognese.pdf']
while x < len(livre):
    e1.append(open(livre[x], 'rb'))
    x = x + 1

x = 0

while x < len(livre):
    e2.append(PyPDF4.PdfFileReader(e1[x]))
    x = x + 1

pdfWriter = PyPDF4.PdfFileWriter()

x= 0 

while x < len(e2):
    for pageNum in range(e2[x].numPages):
        pageObj = e2[x].getPage(pageNum)
        pdfWriter.addPage(pageObj)
    x = x + 1

pdfOutputFile = open('combine.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()

for fermer in e1:
    fermer.close()
   


