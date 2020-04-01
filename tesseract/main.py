from PIL import Image
import pytesseract
from PyPDF2 import PdfFileReader, PdfFileMerger
import io
import os
import os.path


working_dir = r"C:\Users\roger\OneDrive\Desktop\fix_pdf"

pdfs = []
merger = PdfFileMerger()

for dir_entry in os.listdir(working_dir):
    filename, ext = os.path.splitext(dir_entry)
    if not ext == ".jpg":
        continue
    image_path = os.path.join(working_dir, dir_entry)
    image = Image.open(image_path)
    byte_pdf = pytesseract.image_to_pdf_or_hocr(image, extension="pdf")
    pdf_stream = io.BytesIO(byte_pdf)
    pdf = PdfFileReader(pdf_stream)
    pdfs.append(pdf)
    merger.append(pdf)

merger.write(os.path.join(working_dir, "out.pdf"))
merger.close()
