# Importamos PdfReader de la librería PyPDF2
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("archivoencriptado.pdf") # Indicamos el nombre del PDF 
writer = PdfWriter() # Creamos el objeto que utilizaremos para crear un PDF nuevo
# Creamos una condición, donde si el archivo esta encriptado utilizaremos la función decrypt()
if reader.is_encrypted:
    reader.decrypt("bright-labs") # desencriptamos el archivo ingresando su contraseña

#  Añadimos todo el contenido del PDF previo al PDF nuevo
for page in reader.pages:
    writer.add_page(page)

# Guardamos el nuevo archivo PDF
with open("archivodesencriptado.pdf", "wb") as f:
    writer.write(f)