import os
from django.core.exceptions import ValidationError


def allow_only_image_upload(value):
    ex = ["jpg", "jpeg", "png", "gif"]
    ex_valid = os.path.splitext(value.name)[1][1:].lower()

    if not ex in ex_valid:
        raise ValidationError(
            "Only Image files are allowed Allow extensions are: jpg, jpeg, png, gif"
        )


def allow_only_pdf_upload(value):
    ex = ["pdf"]
    ex_valid = os.path.splitext(value.name)[1][1:].lower()

    if not ex in ex_valid:
        raise ValidationError("Only PDF files are allowed Allow extensions are: pdf")


def allow_pdf_image(value):
    ex = ["jpg", "jpeg", "png", "gif", "pdf"]
    ex_valid = os.path.splitext(value.name)[1][1:].lower()

    if not ex in ex_valid:
        raise ValidationError(
            "Only Image and PDF files are allowed Allow extensions are: jpg, jpeg, png, gif,pdf"
        )


from PyPDF2 import PdfFileReader
from PIL import Image

def generate_pdf_thumbnail(pdf_path, output_path, page_number=0):
    pdf = PdfFileReader(open(pdf_path, 'rb'))
    page = pdf.getPage(page_number)
    xObject = page['/Resources']['/XObject'].get_object()
    for obj in xObject:
        if xObject[obj]['/Subtype'] == '/Image':
            img = xObject[obj]
            img_data = img._data
            with open(output_path, 'wb') as f:
                f.write(img_data)
