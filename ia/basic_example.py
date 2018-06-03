# Internet Archive Client
from internetarchive import get_item
from utils.io_parser import IOParser

if __name__ == '__main__':
    parser = IOParser()
    ia_item = get_item(parser.input)
    print(ia_item.metadata)
