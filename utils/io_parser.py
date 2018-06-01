# A canned parser for internet archive examples -- just reads in input and output but can be extended

import argparse


class IOParser(object):
    def __init__(self, **kwargs):
        self.input = None
        self.output = None
        try:
            self.extended_args = kwargs['add_args']
        except KeyError:
            self.extended_args = None

        self.init_parser()

    def init_parser(self):
        parser = argparse.ArgumentParser(description="Test that the reader works")
        parser.add_argument('-i', '--input', help="input value or path", required=True, type=str)
        parser.add_argument('-o', '--output', help="output value or path", required=False, type=str)

        if self.extended_args:
            for arg in self.extended_args:
                parser.add_argument(arg['short'], arg['verbose'], help=arg['help'], required=arg['required'], type=arg['type'])

        args = vars(parser.parse_args())
        for arg in args.items():
            setattr(self, arg[0], arg[1])
