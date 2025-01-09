import os
from flask import Flask, render_template, request, redirect, url_for
import cv2
from PIL import Image
import google.generativeai as genai
from docx import Document

# Configurar a API generativa
genai.configure(api_key="insira key")
model = genai.GenerativeModel("gemini-1.5-flash")

# Configurar o Flask
app = Flask(__name__)

# Pasta para armazenar arquivos enviados
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "Nenhum arquivo enviado", 400

    file = request.files['file']
    if file.filename == '':
        return "Nenhum arquivo selecionado", 400

    # Salvar o arquivo enviado
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Processar a imagem
    try:
        # Ler e processar a imagem
        image = cv2.imread(filepath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 102, 255, cv2.THRESH_BINARY_INV)
        processed_image_path = os.path.join(app.config['UPLOAD_FOLDER'], "imagem_processada.png")
        cv2.imwrite(processed_image_path, thresh)

        # Reconhecer texto usando a API
        text = Image.open(processed_image_path)
        response = model.generate_content(["O que está escrito? Apenas transcreva o texto sem comentar nada", text])

        # Criar o arquivo .docx
        doc = Document()
        style = doc.styles['Normal']
        font = style.font
        font.name = 'Times New Roman'
        text_doc = response.text
        doc.add_paragraph(text_doc)

        # Salvar o documento
        doc_path = os.path.join(app.config['UPLOAD_FOLDER'], "document.docx")
        doc.save(doc_path)

        return redirect(url_for('download_file', filename="document.docx"))

    except Exception as e:
        return f"Erro ao processar a imagem: {e}", 500

@app.route('/uploads/<filename>')
def download_file(filename):
    return f"""
    <h1>Documento gerado com sucesso!</h1>
    <a href="/uploads/{filename}" download>Baixar o documento</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
