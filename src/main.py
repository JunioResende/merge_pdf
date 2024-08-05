import os

from PyPDF2 import PdfMerger


class merge_pdf:
    def __init__(self):
        self.source_path = '/home/junio/progeo/clients/Teste/2024/Teste/maps'

    def list_files(self):
        pdf_list = os.listdir(self.source_path)
        pdf_list.sort()
        return pdf_list

    def merge_files(self, pdf_list):
        merger = PdfMerger()
        for pdf in pdf_list:
            merger.append(self.source_path + '/' + pdf)
        merger.write(self.source_path + '/merged.pdf')
        merger.close()


if __name__ == '__main__':
    merge_pdf = merge_pdf()
    merge_pdf.merge_files(merge_pdf.list_files())
