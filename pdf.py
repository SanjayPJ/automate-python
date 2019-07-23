import PyPDF2, os

os.chdir("C:\\Users\\sam\\Downloads")
pdf_file = open("sample.pdf", 'rb')
reader = PyPDF2.PdfFileReader(pdf_file)
print(reader.numPages)

page = reader.getPage(0)
print(page.extractText())
for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())

writer = PyPDF2.PdfFileWriter()
writer.addPage(page)
for pageNum in range(reader.numPages):
    new_page = reader.getPage(pageNum)
    writer.addPage(new_page)
output = open('new-pdf.pdf', 'wb')
writer.write(output)
output.close()
pdf_file.close()
