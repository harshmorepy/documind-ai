from pypdf import PdfReader


def extract_text(pdf_path):
    """
    Extract text from every page of a PDF.
    """

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text