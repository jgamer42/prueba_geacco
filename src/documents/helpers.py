from PyPDF2 import PdfReader,PdfWriter
import pandas as pd
from fpdf import FPDF
import docx
from io import StringIO 
import re
def handle_pdf(file):
    output = ""
    pdf_reader = PdfReader(file)
    current_page = 0
    while current_page < len(pdf_reader.pages):
        page = pdf_reader.pages[current_page]
        output += page.extract_text()
        current_page += 1
    return output

def handle_docx(file):
    output = ""
    doc = docx.Document(file)
    for para in doc.paragraphs:
        output += para.text
    return output

def handle_excel(file):
    data = pd.read_excel(file)
    return data.to_string(index=False)

def handle_file(file,file_type):
    if file_type=="PDF":
        return handle_pdf(file)
    elif file_type == "XLSX":
        return handle_excel(file)
    elif file_type == "DOCX":
        return handle_docx(file)
    else:
        return ""
    
