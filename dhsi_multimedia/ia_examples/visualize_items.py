# utils
from io_utils import IOParser
from ia_helper import download_files, FORMAT_OPTION, DIR_OPTION, parse_formats, avg_image, extract_jpegs_from_pdf

# os
import os

EXTENSIONS = ['.jpg', '.jpeg', '.JPG', '.JPEG', '.png', '.tif', '.bmp', '.gif', '.tga']
PDF_EXT = '.pdf'

if __name__ == '__main__':
    parser = IOParser(add_args=[FORMAT_OPTION, DIR_OPTION])
    query = parser.input
    outfile = parser.output
    formats = parser.formats
    directory = parser.directory
    paths = []

    if formats:
        paths = download_files(query, directory, formats=parse_formats(formats))
    else:
        paths = download_files(query, directory)
    images = [path for path in paths if os.path.splitext(path)[1] in EXTENSIONS]
    pdfs = [path for path in paths if os.path.splitext(path)[1] == PDF_EXT]

    if len(pdfs) > 0:
        all_jpegs = [extract_jpegs_from_pdf(pdf, directory) for pdf in pdfs]
        images = images + [jpeg for jpegs in all_jpegs for jpeg in jpegs]

    avg_image(images, outfile)
