import PyPDF2

with open('Anushka_Resume .pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    print(text)
