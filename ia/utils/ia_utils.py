# Internet Archive Client
from internetarchive.item import Item, Collection
from internetarchive import search_items

# csv
import csv


IA_URL = 'https://archive.org/details/'


def is_item(val):
    try:
        return type(val).__name__ is Item.__name__
    except AttributeError:
        return False


def is_collection(val):
    try:
        return type(val).__name__ is Collection.__name__
    except AttributeError:
        return False


def export_formats(query, outfile):
    formats = ['Title', 'URL']
    items = []

    try:
        print("Retrieving all items for query: {}".format(query))
        items_count = 1
        for item in search_items('{}'.format(query)).iter_as_items():
            if is_item(item):
                item_info = {}
                item_info['Title'] = item.metadata['title']
                item_info['URL'] = "{}{}".format(IA_URL, item.metadata['identifier'])
                for file in item.item_metadata['files']:
                    format = file['format']
                    if file['format'] not in formats:
                        formats.append(file['format'])
                    if file['format'] not in item_info:
                        item_info[format] = 1
                    else:
                        item_info[format] += 1
                items.append(item_info)
                print('\rTotal items: {}'.format(items_count), end='', flush=True)
                items_count += 1

        with open(outfile, 'w') as csv_output:
            writer = csv.DictWriter(csv_output, fieldnames=formats, extrasaction='ignore')
            writer.writeheader()
            for item in items:
                writer.writerow(item)

    except KeyboardInterrupt:
        print("Writing output to {}".format(outfile))
        with open(outfile, 'w') as csv_output:
            writer = csv.DictWriter(csv_output, fieldnames=formats, extrasaction='ignore')
            writer.writeheader()
            for item in items:
                writer.writerow(item)