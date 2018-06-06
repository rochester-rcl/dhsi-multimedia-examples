# utils
from io_utils import IOParser
from ia_helper import download_files, FORMAT_OPTION, DIR_OPTION, parse_formats, avg_image

if __name__ == '__main__':
    parser = IOParser(add_args=[FORMAT_OPTION, DIR_OPTION])
    query, outfile, formats, directory = parser.get_all_arguments()
    paths = []
    if formats:
        paths = download_files(query, directory, formats=parse_formats(formats))
    else:
        paths = download_files(query, directory)

    avg_image(paths, outfile)