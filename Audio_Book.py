import pyttsx3
import PyPDF2
book = open('C:\\Users\\1035141\\Documents\\Python_Pratice\\pdf_file.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(0,pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say('Hello')
    speaker.runAndWait()