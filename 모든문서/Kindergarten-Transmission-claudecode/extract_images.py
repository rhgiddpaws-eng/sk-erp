import fitz # PyMuPDF
import os

pdf_path = r"d:\BBB WISHCAT PROGECT BBB2\Kindergarten-Transmission-claudecode\모든문서\시작문서\참조할문서-이미지-링크\문서\유치원아이큐브매뉴얼.pdf"
doc = fitz.open(pdf_path)
for page_num in range(min(5, len(doc))): # Extract first 5 pages, mainly the UI ones. Wait, the main UI is on page 10? Let's extract pages 8 to 15.
    page = doc.load_page(page_num)
    pix = page.get_pixmap(dpi=150)
    output_path = f"page_{page_num}.png"
    pix.save(output_path)
    print(f"Saved {output_path}")
