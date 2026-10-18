import os
import pypdfium2 as pdfium

pdf_path = r"docs\RailSahayak_Stakeholder_Presentation.pdf"
output_dir = r"docs\presentation_qa_images"
os.makedirs(output_dir, exist_ok=True)

pdf = pdfium.PdfDocument(pdf_path)
print(f"Total pages in PDF: {len(pdf)}")

image_paths = []
for i, page in enumerate(pdf):
    # Render at 150 DPI (scale=150/72 ≈ 2.083) for crisp inspection
    image = page.render(scale=2.0).to_pil()
    img_filename = f"slide_{i+1:02d}.png"
    img_path = os.path.join(output_dir, img_filename)
    image.save(img_path)
    image_paths.append(img_path)
    print(f"Rendered Page {i+1} -> {img_path} ({image.width}x{image.height}px)")

print(f"All {len(image_paths)} pages rendered successfully!")
