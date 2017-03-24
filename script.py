#!/usr/bin/python

import sys
import csv
from PyPDF2 import PdfFileReader, PdfFileWriter

csvpath = sys.argv[0]
pdfpath = sys.argv[1]

pdf = PdfFileReader(open(pdfpath, 'rb'))

with open(csvpath, 'rb') as csvfile:
    table = csv.DictReader(csvfile)

    for row in table:
        pages = map(int, row['page'].split('-'))
        if len(pages) > 1:
            pages = range(pages[0], pages[1] + 1)

        result = PdfFileWriter()

        for page in pages:
            result.addPage(pdf.getPage(page))
        result.addMetadata(row)

        out = file('%(name)s.pdf' % row['subject'], 'wb')
        result.write(out)
        out.close()
