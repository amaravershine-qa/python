from pypdf import PdfReader

def pdf_reader(file_path):
    """
    Reads a pdf file and extracts text from it
    """
    reader = PdfReader(file_path)

    total_pages = len(reader.pages)

    print(f"Total number of pages in the document: {total_pages}")

    for index,page in enumerate(reader.pages):
        text = page.extract_text()
        print(f"-----Page {index+1} ------")
        print(text if text else "No text found on this page.")
        print("\n")

if __name__ == "__main__":
    pdf_path = "/Users/aditi/Downloads/Amar_Kumar_Resume_Final.pdf"
    pdf_reader(pdf_path)
