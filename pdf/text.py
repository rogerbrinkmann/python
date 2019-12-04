import PyPDF2
import os.path

outfilename = "output.txt"
outfile = open(outfilename, "w", encoding='utf-8')
filepath = rf"{os.path.dirname(os.path.abspath(__file__))}\text.pdf"
pdf_file = open(filepath, 'rb')
pdf = PyPDF2.PdfFileReader(pdf_file)

num_pages = pdf.getNumPages()

for page_num in range(num_pages):
    indentation = 0
    outfile.write(f"{'Page:':>{indentation}}{page_num:<1}\n")
    
    page = pdf.getPage(page_num)
    

    page_text = page.extractText()
    outfile.write(page_text)
    print(page_text)


pdf_file.close()
outfile.close()
