"""
Render all pages of docs/RailSahayak_Stakeholder_Proposal.pdf to high-resolution PNG images
for visual QA and verification.
"""

import os
import pypdfium2 as pdfium

BASE_DIR = r"C:\Railshahayak\railsahayak-backend-starter\railsahayak-backend-starter"
PDF_PATH = os.path.join(BASE_DIR, "docs", "RailSahayak_Stakeholder_Proposal.pdf")
OUT_DIR = os.path.join(BASE_DIR, "docs", "proposal_qa_images")

def render_pages():
    os.makedirs(OUT_DIR, exist_ok=True)
    pdf = pdfium.PdfDocument(PDF_PATH)
    total_pages = len(pdf)
    print(f"Total pages in Proposal PDF: {total_pages}")
    
    for i in range(total_pages):
        page = pdf[i]
        # Render at 150 DPI for high-res A4 inspection (A4 at 150 dpi is ~1240x1754 px)
        image = page.render(scale=150 / 72).to_pil()
        out_file = os.path.join(OUT_DIR, f"page_{i+1:02d}.png")
        image.save(out_file)
        print(f"Rendered Page {i+1} -> {out_file} ({image.width}x{image.height}px)")
        
    print(f"All {total_pages} pages rendered successfully to {OUT_DIR}")

if __name__ == "__main__":
    render_pages()
