import os
from pypdf import PdfReader, PdfWriter
def split_pages(input_pdf_path,output_directory="split_pages"):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    reader = PdfReader(input_pdf_path)
    total_pages  = len(reader.pages)
    for index, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        output_pdf_path = os.path.join(output_directory, f"page_{index+1}.pdf")
        with open(output_pdf_path, "wb") as output_pdf:
            writer.write(output_pdf)
        print(f"Page {index+1} saved as {output_pdf_path}")
if __name__ == "__main__":
    split_pages("/Users/aditi/Documents/Python Practise/generated/classified_officer_ranks.pdf")
