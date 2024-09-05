# importing required modules
from pypdf import PdfReader

# creating a pdf reader object
reader = PdfReader('IT.pdf')

# printing number of pages in pdf file
print(len(reader.pages))

# getting a specific page from the pdf file
page = reader.pages[0]

# extracting text from page
text = page.extract_text()
print(text)
