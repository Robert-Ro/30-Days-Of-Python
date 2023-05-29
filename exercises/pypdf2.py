from PyPDF2 import PdfReader

reader = PdfReader("cxy.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[7]
text = page.extract_text()
# .encode('utf-8')

print(text)