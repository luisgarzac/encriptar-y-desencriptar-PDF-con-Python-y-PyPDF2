# Importamos PdfReader de la librería PyPDF2
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("archivo1.pdf") # Indicamos el nombre del PDF 
writer = PdfWriter() # Creamos el objeto que utilizaremos para crear un PDF nuevo

#  Añadimos todo el contenido del PDF previo al PDF nuevo
for page in reader.pages:
    writer.add_page(page)

# Añadimos una contraseña al nuevo PDF
writer.encrypt("bright-labs")

# Guardamos el nuevo archivo PDF
with open("archivoencriptado.pdf", "wb") as f:
    writer.write(f)