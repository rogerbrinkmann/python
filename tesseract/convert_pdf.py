import io

import struct
import os
import os.path
from collections import defaultdict
from PIL import Image
import pytesseract
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.utils import PdfReadError
import logging
import chardet

logging.basicConfig(filename='logger.log', filemode='w', level=logging.DEBUG)

def NestedDict():
    return defaultdict(NestedDict)


class ImageExtractor:

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

    def get_image(self, pdf_file_path):
        num_pages = 0
        with open(pdf_file_path, "rb") as pdf_file:
            pdf_reader = PdfFileReader(pdf_file)
            try:
                num_pages = pdf_reader.getNumPages()
            except PdfReadError as readerr:
                logging.debug(f"{readerr} in {pdf_file}")
                return
            except Exception as e:
                logging.debug(f"{e} in {pdf_file}")

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
                            logging.debug(f"{e} in {pdf_file_path}")
                            return
                        yield image
                    elif "/DCTDecode" in vobj["/Filter"]:
                        # A compressed image
                        try:
                            image = Image.open(io.BytesIO(vobj._data))
                        except Image.UnidentifiedImageError as e:
                            logging.debug(f"{e} in {pdf_file_path}")
                            return
                        yield image
                        

                    elif "/CCITTFaxDecode" in vobj["/Filter"]:
                        if vobj["/DecodeParms"][0]["/K"] == -1:
                            CCITT_group = 4
                        else:
                            CCITT_group = 3
                        width = vobj["/Width"]
                        height = vobj["/Height"]
                        data = vobj._data
                        img_size = len(data)
                        tiff_header = self.tiff_header_for_CCITT(
                            width, height, img_size, CCITT_group
                        )
                        try:
                            image = Image.open(io.BytesIO(tiff_header + data))
                        except Exception as e:
                            logging.debug(f"{e} in {pdf_file_path}")
                            return
                        yield image
                    else:
                        try:
                            image = Image.open(io.BytesIO(vobj._data))
                        except Exception as e:
                            logging.debug(f"{e} in {pdf_file_path}")
                            return
                        yield image

def isreadable(pdf_file_path):
    num_pages = 0
    with open(pdf_file_path, "rb") as pdf_file:
        pdf_reader = PdfFileReader(pdf_file)
        try:
            num_pages = pdf_reader.getNumPages()
        except PdfReadError as readerr:
            logging.debug(f"{readerr} in {pdf_file_path}")
            return False
        except Exception as e:
            logging.debug(f"{e} in {pdf_file_path}")

        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()
            if text:
                return True
    return False
            

extractor = ImageExtractor()


def find_pdf(root_path):
    for root, _, files in os.walk(root_path):
        for file in files:
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)
            if ext != ".pdf":
                continue
            yield file_path

        
for file_path in find_pdf(r"C:\Users\roger\Google Drive\Agi"):    
    if isreadable(file_path):
        logging.debug(f"{file_path} is readable")
        continue
    images = []
    for image in extractor.get_image(file_path):
        images.append(image)
    logging.debug(f"Found {len(images)} in {file_path}")
