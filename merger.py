from pypdf import PdfWriter
import os

# merger
merger = PdfWriter()

# directory of the original PDF files
dir_original = "./pdf_original"

# list of file names
name_list = []

print("Find PDF files:")
# enumerate through the origional directory
for idx, file_name in enumerate(os.listdir(dir_original)):
    if file_name.endswith(".pdf"):
        print(f'{idx+1}. {file_name}')
        name_list.append(file_name)

# input the merging order
file_order = input ("Enter the Merging Order (ex: 1, 3, 2, ...):")
file_order = file_order.split(",")

# check input length
if(len(file_order)!=len(name_list)):
    raise Exception("Invaild Merging Order!")

# merge file according to the order
for index in file_order:
    dir_file = os.path.join(dir_original, name_list[int(index)-1])
    merger.append(dir_file)
merger.write("./pdf_merged/merged-pdf.pdf")
merger.close()
print("Successfully Merge!")