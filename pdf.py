#!/usr/bin/env python3

import os
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

fruits = {
  "watermelon": 1,
  "strawberries": 9,
  "apples": 3,
  "durians": 2,
  "bananas": 6,
  "mangos": 3,
  "kiwis": 6
}

report = SimpleDocTemplate("report.pdf")
styles = getSampleStyleSheet()

report_title = Paragraph("Inventory of my fruits", styles["h1"])
report.build([report_title])

table_data = []
for k, v in fruits.items():
    table_data.append([k, v])

table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]

# testing
# print(table_data)

report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
report.build([report_title, report_table])

print("Pdf created!")
