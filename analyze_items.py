# Internet Archive Client
from internetarchive import search_items
from utils.io_parser import IOParser
from utils.ia_utils import is_item, is_collection
import csv

if __name__ == '__main__':
    parser = IOParser()
    formats = ['Title']
    items = []
    try:
        for item in search_items('{}'.format(parser.input)).iter_as_items():
            if is_item(item):
                item_info = {}
                item_info['Title'] = item.metadata['title']
                for file in item.item_metadata['files']:
                    format = file['format']
                    if file['format'] not in formats:
                        formats.append(file['format'])
                    if file['format'] not in item_info:
                        item_info[format] = 1
                    else:
                        item_info[format] += 1
                items.append(item_info)

        with open(parser.output, 'w') as csv_output:
            writer = csv.DictWriter(csv_output, fieldnames=formats, extrasaction='ignore')
            writer.writeheader()
            for item in items:
                writer.writerow(item)

    except KeyboardInterrupt:

        with open(parser.output, 'w') as csv_output:
            writer = csv.DictWriter(csv_output, fieldnames=formats, extrasaction='ignore')
            writer.writeheader()
            for item in items:
                writer.writerow(item)

