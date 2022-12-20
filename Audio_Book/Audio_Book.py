import pyttsx3
import PyPDF2
book = open("E:\\Python_Pratics\\Audio_Book\\batch.pdf",'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
speaker = pyttsx3.init()
for i in range(10,pages):
    page=pdfReader.getPage(i)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()
