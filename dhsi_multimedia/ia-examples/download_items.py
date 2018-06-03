# utils
from io_utils import IOParser
from ia_helper import download_files, FORMAT_OPTION, parse_formats

if __name__ == '__main__':
    parser = IOParser(add_args=[FORMAT_OPTION])
    query, outdir, formats = parser.get_all_arguments()
    if formats:
        download_files(query, outdir, formats=parse_formats(formats))
    else:
        download_files(query, outdir)