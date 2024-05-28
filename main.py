import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

def add_page_numbers(pdf_path, output_path):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    temp_files = []
    for i in range(len(reader.pages)):
        if i != 0:  # 1ページ目をスキップ
            temp_pdf_path = f"temp_page_{i + 1}.pdf"
            temp_files.append(temp_pdf_path)
            
            c = canvas.Canvas(temp_pdf_path, pagesize=letter)
            width, height = letter

            # フォント設定
            c.setFont("Helvetica-Bold", 20)

            # ページ番号の背景を描画
            text = str(i + 1)
            text_width = c.stringWidth(text, "Helvetica-Bold", 20)
            x_position = 20
            y_position = 20
            padding_side = 10  # サイドのパディング
            padding_top = 5  # トップのパディング
            padding_bottom = 10  # ボトムのパディング
            c.setFillColor(colors.black)
            c.rect(x_position - padding_side, y_position - padding_bottom, text_width + 2 * padding_side, 20 + padding_top + padding_bottom, fill=1)

            # ページ番号を描画
            c.setFillColor(colors.white)
            c.drawString(x_position, y_position, text)

            c.save()

            temp_reader = PdfReader(temp_pdf_path)
            page = reader.pages[i]
            page.merge_page(temp_reader.pages[0])
        else:
            # 1ページ目はそのまま追加
            page = reader.pages[i]

        writer.add_page(page)
    
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)

    for temp_file in temp_files:
        os.remove(temp_file)

# 使用方法
input_pdf_path = "input.pdf"  # 追加したいPDFファイルのパス
output_pdf_path = "output_with_page_numbers.pdf"  # 出力ファイルのパス
add_page_numbers(input_pdf_path, output_pdf_path)
