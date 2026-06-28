from backend.app.pdf_reader import extract_text

pdf_text = extract_text("data/pdfs/python_notes.pdf")

# print(pdf_text)
print("=" * 80)
print("Extracted PDF Text")
print("=" * 80)
print(pdf_text)
