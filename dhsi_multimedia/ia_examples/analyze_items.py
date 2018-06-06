# utils
from io_utils import IOParser
from ia_helper import file_info_to_csv, FORMAT_OPTION, parse_formats

if __name__ == '__main__':
    parser = IOParser(add_args=[FORMAT_OPTION])
    query = parser.input
    outfile = parser.output
    formats = parser.formats
    if formats:
        file_info_to_csv(query, outfile, formats=parse_formats(formats))
    else:
        file_info_to_csv(query, outfile)
