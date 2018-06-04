# utils
from io_utils import IOParser
from ia_helper import plot_items, FORMAT_OPTION, parse_formats

if __name__ == '__main__':
    parser = IOParser(add_args=[FORMAT_OPTION])
    query, outfile, formats = parser.get_all_arguments()
    if formats:
        plot_items(query, outfile, formats=parse_formats(formats))
    else:
        plot_items(query, outfile)
