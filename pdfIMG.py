from pdf2image import convert_from_path
import pytesseract
from pdf2docx import Converter
from docx import Document

pdf_file = "/home/churros/Área de trabalho/teste/Digitalizado_20241127-1942.pdf"


images = convert_from_path(pdf_file)

ocr_text = ""
for image in images:
    ocr_text += pytesseract.image_to_string(image)

print(ocr_text)

docx_file = "/home/churros/Área de trabalho/teste/resultado/digitado.docx"
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()

doc = Document(docx_file)
doc.add_paragraph(ocr_text)

doc.save("/home/churros/Área de trabalho/teste/resultado/digitado_editado.docx")
