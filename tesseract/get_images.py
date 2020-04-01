import minecart
from PIL import Image
import os
import io

import struct
import os.path
from collections import defaultdict
from PIL import Image
import pytesseract
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.utils import PdfReadError
import logging
import chardet

logging.basicConfig(filename='logger.log', filemode='w', level=logging.INFO)

def find_pdf(root_path):
    for root, _, files in os.walk(root_path):
        for file in files:
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)
            if ext != ".pdf":
                continue
            yield file_path

def has_text(doc):
    for page in doc.iter_pages():
        if page.letterings:
            return True
    return False

def tiff_header_for_CCITT(self, width, height, size, CCITT_group=4):
        tiff_header_struct = "<" + "2s" + "h" + "l" + "h" + "hhll" * 8 + "h"
        return struct.pack(
            tiff_header_struct,
            b"II",  # Byte order indication: Little indian
            42,  # Version number (always 42)
            8,  # Offset to first IFD
            8,  # Number of tags in IFD
            256,
            4,
            1,
            width,  # ImageWidth, LONG, 1, width
            257,
            4,
            1,
            height,  # ImageLength, LONG, 1, lenght
            258,
            3,
            1,
            1,  # BitsPerSample, SHORT, 1, 1
            259,
            3,
            1,
            CCITT_group,  # Compression, SHORT, 1, 4 = CCITT Group 4 fax encoding
            262,
            3,
            1,
            0,  # Threshholding, SHORT, 1, 0 = WhiteIsZero
            273,
            4,
            1,
            struct.calcsize(tiff_header_struct),  # StripOffsets, LONG, 1, len of header
            278,
            4,
            1,
            height,  # RowsPerStrip, LONG, 1, lenght
            279,
            4,
            1,
            size,  # StripByteCounts, LONG, 1, size of image
            0,  # last IFD
        )

for pdf_file_path in find_pdf(r"C:\Users\roger\Google Drive"):
    images = []
    print(pdf_file_path)
    with open(pdf_file_path, "rb") as pdf_file:
        try:
            doc = minecart.Document(pdf_file)
        except Exception as e:
            logging.error(f"{e} in {pdf_file_path}")

        if has_text(doc):
            logging.info(f"text: {pdf_file_path}")
            continue

        for num_pages, page in enumerate(doc.iter_pages(), 1):
            for image in page.images:
                try:
                    pil_image = image.as_pil()
                    images.append(pil_image)
                except Exception as e:
                    logging.error(f"{e} in {pdf_file_path}")
        if images:
            logging.info(f"images {len(images)}: {pdf_file_path}")
            continue

        pdf_reader = PdfFileReader(pdf_file)
        try:
            num_pages = pdf_reader.getNumPages()
        except PdfReadError as readerr:
            logging.info(f"{readerr} in {pdf_file_path}")
            continue
        except Exception as e:
            logging.error(f"{e} in {pdf_file_path}")

        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            resources = page["/Resources"]
            if "/XObject" not in resources:
                continue
            for value in resources["/XObject"].values():
                vobj = value.getObject()
                # We are only interested in images...
                if vobj["/Subtype"] != "/Image" or "/Filter" not in vobj:
                    continue
                if vobj["/Filter"] == "/FlateDecode":
                    # A raw bitmap
                    buf = vobj.getData()
                    # Notice that we need metadata from the object
                    # so we can make sense of the image data
                    size = tuple(map(int, (vobj["/Width"], vobj["/Height"])))
                    try:
                        image = Image.frombytes("RGB", size, buf, decoder_name="raw")
                    except ValueError as e:
                        logging.error(f"{e} in {pdf_file_path}")
                        continue
                    images.append(image)
                elif "/DCTDecode" in vobj["/Filter"]:
                    # A compressed image
                    try:
                        image = Image.open(io.BytesIO(vobj._data))
                    except Image.UnidentifiedImageError as e:
                        logging.info(f"{e} in {pdf_file_path}")
                        continue
                    images.append(images)
                elif "/CCITTFaxDecode" in vobj["/Filter"]:
                    if vobj["/DecodeParms"][0]["/K"] == -1:
                        CCITT_group = 4
                    else:
                        CCITT_group = 3
                    width = vobj["/Width"]
                    height = vobj["/Height"]
                    data = vobj._data
                    img_size = len(data)
                    tiff_header = tiff_header_for_CCITT(
                        width, height, img_size, CCITT_group
                    )
                    try:
                        image = Image.open(io.BytesIO(tiff_header + data))
                    except Exception as e:
                        logging.error(f"{e} in {pdf_file_path}")
                        continue
                    images.append(image)
                else:
                    try:
                        image = Image.open(io.BytesIO(vobj._data))
                    except Exception as e:
                        logging.error(f"{e} in {pdf_file_path}")
                        continue
                    images.append(image)
 
    logging.info(f"images {len(images)}: {pdf_file_path}")
