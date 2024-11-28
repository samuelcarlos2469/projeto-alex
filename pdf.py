from pdf2docx import Converter

pdf_file = "/home/churros/Área de trabalho/teste/Ruan Wallacy Mendes Costa.pdf"

docx_file = "/home/churros/Área de trabalho/teste/resultado/ruan.docx"

cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()
