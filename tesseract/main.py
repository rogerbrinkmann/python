from PIL import Image
import pytesseract
from PyPDF2 import PdfFileReader, PdfFileWriter
import io
import os.path


def print_idata(idata):
    rows = idata.splitlines()
    print(rows[0])
    for row in rows[1:]:
        rest, posx, posy, width, height, conf, text = row.rsplit("\t", 6)
        if int(conf) > 70:
            print(row)


def get_images_from_pdf(pdf_path):
    images = []
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PdfFileReader(pdf_file)
        num_pages = pdf_reader.getNumPages()
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)

            # Images are part of a page's `/Resources/XObject`
            r = page["/Resources"]
            if "/XObject" not in r:
                continue
            for k, v in r["/XObject"].items():
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
    return images


def get_pdf_from_image(image):
    # text = pytesseract.image_to_string(image), lang='deu')
    # print(text)
    # bbox = pytesseract.image_to_boxes(image), lang='deu')
    # print(bbox)
    idata = pytesseract.image_to_data(image, lang="deu")
    print_idata(idata)
    # osd = pytesseract.image_to_osd(image), lang='deu')
    # print(osd)
    pdf = pytesseract.image_to_pdf_or_hocr(image, extension="pdf")
    return pdf


def get_pdfs_from_images(images):
    pdfs = []
    for image in images:
        pdf = pytesseract.image_to_pdf_or_hocr(image, extension="pdf")
        pdfs.append(pdf)
    return pdfs


def save_pdf(pdf_path, pdf):
    writer = PdfFileWriter()
    writer.addPage(pdf)
    with open(pdf_path, "w+b") as f:
        writer.write(f)


def get_images_from_image_paths(image_paths):
    images = []
    for image_path in image_paths:
        image = Image.open(image_path)
        images.append(image)
    return images


if __name__ == "__main__":
    image_paths = [
        r"C:\Repos\python\tesseract\Clipboard01.jpg",
        r"C:\Repos\python\tesseract\Clipboard02.jpg",
    ]
    images = get_images_from_image_paths(image_paths)
    pdfs = get_pdfs_from_images(images)

    writer = PdfFileWriter()
    for pdf in pdfs:
        writer.addPage(pdf)

    with open(r"C:\Repos\python\tesseract\Clipboard01.jpg", 'wb') as f:
        write.write(f)

    # pdf_path = r"C:\Repos\python\tesseract\20150209_Bussgeldbescheid.pdf"
    head, tail = os.path.split(pdf_path)
    new_pdf_path = os.path.join(head, "s_" + tail)
    images = get_images_from_pdf(pdf_path)
    for image in images:
        pdf = get_pdf_from_image(image)
        save_pdf(new_pdf_path, pdf)
