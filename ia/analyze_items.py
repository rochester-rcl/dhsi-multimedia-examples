# utils
from utils.io_parser import IOParser
from utils.ia_utils import export_formats

if __name__ == '__main__':
    parser = IOParser()
    query, outfile = parser.get_all_arguments()
    export_formats(query, outfile)

