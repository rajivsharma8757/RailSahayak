import re

file_path = r"scripts\generate_presentation.py"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace Rupee symbol with Rs.
text = text.replace("\u20b9", "Rs. ")

# Add VALIGN TOP to all inner card tables
target1 = "('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),"
repl1 = "('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),\n                ('VALIGN', (0,0), (-1,-1), 'TOP'),"
text = text.replace(target1, repl1)

target2 = "('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#1E5591')),"
repl2 = "('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#1E5591')),\n                ('VALIGN', (0,0), (-1,-1), 'TOP'),"
text = text.replace(target2, repl2)

target3 = "('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#475569')),"
repl3 = "('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#475569')),\n                ('VALIGN', (0,0), (-1,-1), 'TOP'),"
text = text.replace(target3, repl3)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Applied VALIGN TOP and Rs. fix to scripts/generate_presentation.py successfully.")
