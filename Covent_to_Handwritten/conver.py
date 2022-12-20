import PyPDF2
book = open(r'E:\Python_Pratics\Covent_to_Handwritten\sheeft.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages  = pdfreader.numPages
print('Total number of Pages is ',pages)
