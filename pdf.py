from docx import Document
import PyPDF2

def pdf_to_word(pdf_file, word_file):
    try:
        # Abrindo o arquivo PDF
        with open(pdf_file, 'rb') as pdf:
            reader = PyPDF2.PdfReader(pdf)
            document = Document()
            
            # Extraindo texto de cada página
            for page in reader.pages:
                text = page.extract_text()
                document.add_paragraph(text)
            
            # Salvando o conteúdo no arquivo Word
            document.save(word_file)
            print(f"Conversão concluída! O arquivo Word foi salvo como: {word_file}")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Nome dos arquivos
pdf_file = "document.pdf"  # Substitua pelo nome do seu arquivo PDF
word_file = "seu_arquivo.docx"  # Nome para o arquivo Word gerado

# Chamando a função
pdf_to_word(pdf_file, word_file)
