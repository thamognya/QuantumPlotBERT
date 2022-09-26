from doctest import OutputChecker
from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

class PdfToTextClass:

    def __init__(self, dirToPdf=""):
        self.dirToPdf = dirToPdf

    def setDirToPdf(self, dirToPdf):
        self.dirToPdf = dirToPdf

    def convertPdfToText(self):
        output_string = StringIO()
        with open(self.dirToPdf, 'rb') as fin:
            extract_text_to_fp(fin, output_string)
        return output_string.getvalue().strip()

pdf = PdfToTextClass()
pdf.setDirToPdf("/home/jeff/Downloads/PlotBERTBooks/Atomic Habits An Easy Proven Way to Build Good Habits Break Bad Ones (James Clear) (z-lib.org).pdf")
print(pdf.convertPdfToText())