# Pacotes
# Conjuntos de modulos
# Iremos utilizar o PIP gerenciador de pacotes
# pip install pyqrcode

import pyqrcode as qr  # Criamos um alias para o pacote pyqrcode isso evita ter que usar a palavra inteira sempre
from PIL import Image

qrcode = qr.create("https://www.linkedin.com/in/devgabrielpires/")  # String a ser transformada em QRcode
qrcode.png("images/QRcode.png", scale=6)  # Salvando o QR Code
im = Image.open('images/QRcode.png')  # Exibindo o QRcode gerado
im.show()