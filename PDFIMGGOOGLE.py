import cv2
import PIL.Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyBq2nc05mUMNpuyQMsW-j69L7Qtl-Chf0A")
model = genai.GenerativeModel("gemini-1.5-flash")

image_path = "Captura2.png"
image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 102, 255, cv2.THRESH_BINARY_INV)

cv2.imwrite("imagem_processada.png", thresh)


text = PIL.Image.open("imagem_processada.png")
response = model.generate_content(["O que está escrito?", text])
print(response.text)




