import os
import sys

def extract_text_from_pdf(pdf_path):
    try:
        import PyPDF2
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for i in range(min(5, len(reader.pages))): # read first 5 pages max
                text += reader.pages[i].extract_text() + "\n"
            return text
    except ImportError:
        try:
            import fitz # PyMuPDF
            doc = fitz.open(pdf_path)
            text = ""
            for i in range(min(5, doc.page_count)):
                text += doc[i].get_text() + "\n"
            return text
        except ImportError:
            return "No PDF extraction library available (tried PyPDF2 and fitz)."
    except Exception as e:
        return f"Error extracting from {pdf_path}: {e}"

pdf_dir = r"d:\BBB WISHCAT PROGECT BBB2\Kindergarten-Transmission-claudecode\모든문서\시작문서\참조할문서-이미지-링크\문서"
files = ["유치원아이큐브매뉴얼.pdf", "메인사이트.pdf", "1 (2).pdf", "2 (2).pdf", "3 (2).pdf", "4 (2).pdf"]

for f in files:
    path = os.path.join(pdf_dir, f)
    print(f"--- Extracting {f} ---")
    print(extract_text_from_pdf(path)[:500])
    print("---------------------------------\n")

