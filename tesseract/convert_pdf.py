import io
import shutil
import struct
import os
import os.path
from collections import defaultdict
from PIL import Image
import pytesseract
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.utils import PdfReadError

def NestedDict():
    return defaultdict(NestedDict)

def tiff_header_for_CCITT(width, height, img_size, CCITT_group=4):
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
        img_size,  # StripByteCounts, LONG, 1, size of image
        0,  # last IFD
    )


for root, dirs, files in os.walk(r"C:\Users\roger\Google Drive"):
    for file in files:
        file_path = os.path.join(root, file)
        file_name, ext = os.path.splitext(file)
        if ext != ".pdf":
            continue
        pdf_content = NestedDict()
        with open(file_path, "rb") as pdf_file:
            pdf_reader = PdfFileReader(pdf_file)
            try:
                num_pages = pdf_reader.getNumPages()
            except PdfReadError as readerr:
                print(readerr)
                destination = os.path.join(r"C:\Storage", file)
                comment_txt = os.path.join(r"C:\Storage", file_name + ".txt")
                dest = shutil.copyfile(file_path, destination)
                with open(comment_txt, "w") as textfile:
                    textfile.write(root)
                continue
            except Exception as e:
                print(e)

            for page_num in range(num_pages):
                page = pdf_reader.getPage(page_num)
                page_text = page.extractText()
                # Images are part of a page's `/Resources/XObject`
                resources = page["/Resources"]
                contents = page["/Contents"]
                if "/XObject" not in resources:
                    continue
                for k, v in resources["/XObject"].items():
                    vobj = v.getObject()
                    # We are only interested in images...
                    if vobj["/Subtype"] != "/Image" or "/Filter" not in vobj:
                        continue
                    if vobj["/Filter"] == "/FlateDecode":
                        # A raw bitmap
                        buf = vobj.getData()
                        # Notice that we need metadata from the object
                        # so we can make sense of the image data
                        size = tuple(map(int, (vobj["/Width"], vobj["/Height"])))
                        img = Image.frombytes("RGB", size, buf, decoder_name="raw")
                        images.append(img)
                    elif "/DCTDecode" in vobj["/Filter"]:
                        # A compressed image
                        img = Image.open(io.BytesIO(vobj._data))
                        images.append(img)

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
                        img = Image.open(io.BytesIO(tiff_header + data))
                        images.append(img)
                    else:
                        img = Image.open(io.BytesIO(vobj._data))
                        images.append(img)

        for image in images:
            print(image.size)

