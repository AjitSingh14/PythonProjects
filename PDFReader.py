import PyPDF2

PdfFileObj=open('ElectronicTicket.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(PdfFileObj,strict=False)
print(str(pdfReader.numPages))
pageObject=pdfReader.getPage(2)

print(pageObject.extractText())