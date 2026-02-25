import os
import sys

def extract_full_pdf(pdf_path, out_path):
    try:
        import fitz # PyMuPDF
        doc = fitz.open(pdf_path)
        text = ""
        for i in range(doc.page_count):
            text += f"\n--- Page {i+1} ---\n"
            text += doc[i].get_text()
            
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Extraction successful: {doc.page_count} pages written to {out_path}")
    except Exception as e:
        print(f"Error: {e}")

pdf_path = r"d:\BBB WISHCAT PROGECT BBB2\Kindergarten-Transmission-claudecode\모든문서\시작문서\참조할문서-이미지-링크\문서\유치원아이큐브매뉴얼.pdf"
out_path = r"d:\BBB WISHCAT PROGECT BBB2\Kindergarten-Transmission-claudecode\모든문서\결과문서\아이큐브매뉴얼.txt"

extract_full_pdf(pdf_path, out_path)
