"""Create PDF (output_2.pdf) template with lines"""
from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv', sep=';')

for idx, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    for y in range(21, 290, 10):
        pdf.line(10, y, 200, y)

    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=12)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='R')

    for _ in range(row['Pages']):
        pdf.add_page()

        pdf.ln(277)
        pdf.set_font(family='Times', style='I', size=12)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row['Topic'], align='R')
        for y in range(21, 290, 10):
            pdf.line(10, y, 200, y)

pdf.output('output_2.pdf')