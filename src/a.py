from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import re
def generar_pdf_modificado(pdf_path):
    # Crear un objeto PDF
    doc = SimpleDocTemplate("pdf_modificado.pdf", pagesize=letter)

    # Definir estilos
    estilos = getSampleStyleSheet()

    # Leer el contenido original del PDF
    with open(pdf_path, "r") as archivo_pdf:
        contenido_pdf = archivo_pdf.read()

    # Reemplazar el texto del placeholder por el nuevo texto
    expression_to_find = re.findall(r'{{(.*?)}}',contenido_pdf)
    new_text = contenido_pdf
    for expression in expression_to_find:
        new_text = re.sub('{{({})}}'.format(expression),"hola",new_text)

    # Crear una lista de elementos a mostrar en el PDF
    elementos = []

    # Agregar el contenido actualizado al PDF
    elementos.append(Spacer(1, 12))
    for linea in new_text.splitlines():
        p = Paragraph(linea, estilos["Normal"])
        elementos.append(p)

    # Generar el PDF
    doc.build(elementos)

# Uso del método generar_pdf_modificado
if __name__ == "__main__":
    pdf_path = "pruebas.pdf"
    nuevo_texto = "Este es el nuevo texto que reemplazará el placeholder."

    generar_pdf_modificado(pdf_path)