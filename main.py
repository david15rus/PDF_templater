"""Create PDF (output.pdf) template without lines"""
from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv', sep=';')

for idx, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family='Times', style='BI', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L',
             ln=1)
    pdf.line(10, 21, 200, 21)

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=12)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

    for _ in range(1, row['Pages']):
        pdf.add_page()

        # Set the footer
        pdf.ln(277)
        pdf.set_font(family='Times', style='I', size=12)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')
pdf.output('output.pdf')

