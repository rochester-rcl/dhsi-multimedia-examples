# utils
from io_utils import IOParser
from ia_helper import download_files, FORMAT_OPTION, DIR_OPTION, parse_formats, avg_image

# os
import os

EXTENSIONS = ['.jpg', '.jpeg', '.JPG', '.JPEG', '.png', '.tif', '.bmp', '.gif', '.tga']

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
    avg_image(images, outfile)
