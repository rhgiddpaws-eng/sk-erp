import fitz # PyMuPDF
import os

pdf_path = r"d:\BBB WISHCAT PROGECT BBB2\Kindergarten-Transmission-claudecode\모든문서\시작문서\참조할문서-이미지-링크\문서\유치원아이큐브매뉴얼.pdf"
output_dir = "pdf_images"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
for page_num in range(len(doc)): # Extract all pages
    page = doc.load_page(page_num)
    pix = page.get_pixmap(dpi=150)
    output_path = os.path.join(output_dir, f"page_{page_num+1}.png")
    pix.save(output_path)
    print(f"Saved {output_path}")
