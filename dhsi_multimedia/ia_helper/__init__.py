# Internet Archive Client
from internetarchive.item import Item, Collection
from internetarchive import search_items, download

# csv
import csv

IA_URL = 'https://archive.org/details/'

FORMAT_OPTION = {
    'short': '-f',
    'verbose': '--formats',
    'help': 'A comma separated string of formats. For example: JPEG, PNG, MP3',
    'required': False,
    'type': str
}


def parse_formats(formats):
    if ',' in formats:
        return formats.split(',')
    else:
        return [formats]


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


def item_info_has_files(item_info):
    for val in item_info.values():
        if val is not None:
            return True
    return False


def search_files(query, **kwargs):
    filter_formats = None
    if 'formats' in kwargs:
        _formats = kwargs['formats']
        if isinstance(_formats, (list, tuple, set)):
            filter_formats = _formats
        else:
            filter_formats = [_formats]
    meta = ['Title', 'URL', 'Collection', 'ID']
    formats = []
    items = []
    items_count = 1

    def check_format(fformat):
        if filter_formats is None:
            return True
        else:
            return fformat in filter_formats

    def msg():
        nonlocal items_count
        print('\rTotal items: {}'.format(items_count), end='', flush=True)
        items_count += 1

    def format_item(item, **kwargs):
        item_info = {}
        for file in item.item_metadata['files']:
            fformat = file['format']
            valid = check_format(fformat)
            if valid:
                if fformat not in formats:
                    formats.append(file['format'])
                if fformat not in item_info:
                    item_info[fformat] = 1
                else:
                    item_info[fformat] += 1

        if item_info_has_files(item_info):
            item_info['Title'] = item.metadata['title']
            item_info['URL'] = "{}{}".format(IA_URL, item.metadata['identifier'])
            item_info['ID'] = item.metadata['identifier']
            item_info['Collection'] = item.metadata['collection'][0] if isinstance(item.metadata['collection'],
                                                                                   list) else \
            item.metadata['collection']
            items.append(item_info, )
            msg()

    def format_collection(collection):
        for item in collection.contents():
            format_item(item, collection=collection.metadata['identifier'])

    try:
        print("Retrieving all items for query: {}".format(query))

        for result in search_items('{}'.format(query)).iter_as_items():
            if is_item(result):
                format_item(result)

            if is_collection(result):
                format_collection(result)

        return items, formats, meta

    except KeyboardInterrupt:
        print("Stopping search ...")
        return items, formats


def file_info_to_csv(query, outfile, **kwargs):
    items, formats, meta = search_files(query, **kwargs)
    print("Writing results to {}".format(outfile))
    with open(outfile, 'w') as csv_output:
        writer = csv.DictWriter(csv_output, fieldnames=meta+formats, extrasaction='ignore')
        writer.writeheader()
        for item in items:
            writer.writerow(item)


def download_files(query, folder, **kwargs):
    items, formats = search_files(query, **kwargs)
    for item in items:
        download(item['ID'], destdir=folder, formats=formats)

