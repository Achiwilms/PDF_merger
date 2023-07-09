from pypdf import PdfWriter
import os

merger = PdfWriter()
# merger = PyPDF.PdfFileMerger()
dir_original = "./pdf_original"

for file_name in os.listdir(dir_original):
    if file_name.endswith(".pdf"):
        dir_file = os.path.join(dir_original, file_name)
        merger.append(dir_file)
merger.write("./pdf_merged/merged-pdf.pdf")
merger.close()