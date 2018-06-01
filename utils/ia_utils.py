# Internet Archive Client
from internetarchive.item import Item, Collection


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