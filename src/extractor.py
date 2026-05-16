import PyPDF2
import pdfplumber
from docx import Document

def extract_text(file_path):

    text = ""

    # TXT FILE
    if file_path.endswith(".txt"):

        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

    # PDF FILE
    elif file_path.endswith(".pdf"):

        try:
            with pdfplumber.open(file_path) as pdf:

                for page in pdf.pages:
                    extracted = page.extract_text()

                    if extracted:
                        text += extracted

        except:

            with open(file_path, "rb") as file:

                reader = PyPDF2.PdfReader(file)

                for page in reader.pages:

                    extracted = page.extract_text()

                    if extracted:
                        text += extracted

    # DOCX FILE
    elif file_path.endswith(".docx"):

        doc = Document(file_path)

        for para in doc.paragraphs:
            text += para.text + "\n"

    return text