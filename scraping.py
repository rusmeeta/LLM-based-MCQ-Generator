import pymupdf

# Open PDF
doc = pymupdf.open("Zoology.pdf")

print("Total pages:", len(doc))

# Extract Chapter 1
text = ""

for page_number in range(57):
    text += doc[page_number].get_text() + "\n"

doc.close()

# Check the extracted text
print("Characters extracted:", len(text))
print(text[:10000])