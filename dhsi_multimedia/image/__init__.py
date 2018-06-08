import os
from PyPDF2 import PdfFileReader
from io_utils import IOParser

def extract_jpegs_from_pdf(pdf_file, dirname):
    start_hex = b"\xff\xd8"
    start_fix = 0
    end_hex = b"\xff\xd9"
    end_fix = 2
    i = 0
    jpegs = []
    basename = os.path.basename(pdf_file)
    outdir = os.path.join(os.path.abspath(dirname), basename)
    with open(pdf_file, 'rb') as pdf:
        pdf_reader = PdfFileReader(pdf)
        npages = pdf_reader.getNumPages()
        njpg = 0
        _pdf = pdf.read()
        if _pdf is not None:
            while njpg <= npages:
                stream = _pdf.find(b'stream', i)
                start = _pdf.find(start_hex, stream, stream + 20)
                if start < 0:
                    i = stream + 20
                    continue
                end = _pdf.find(b'endstream', start)

                if end < 0:
                    raise Exception("Can't find end of stream!")

                end = _pdf.find(end_hex, end - 20)

                if end < 0:
                    raise Exception("Can't find end of jpeg!")

                start += start_fix
                end += end_fix

                jpg = pdf[start:end]
                filename = '{}/{:04d}.jpg'.format(outdir, njpg)
                with open(filename, 'wb') as outfile:
                    outfile.write(jpg)
                    outfile.close()
                jpegs.append(filename)
                njpg += 1
                i = end
        return jpegs

