from io_utils import IOParser
from image import extract_jpegs_from_pdf
if __name__ == '__main__':
    parser = IOParser()
    infile = parser.input
    directory = parser.output

    extract_jpegs_from_pdf(infile, directory)