from io_utils import IOParser
from ia_helper import avg_image, DIR_OPTION
import os
if __name__ == '__main__':
    parser = IOParser(add_args=[DIR_OPTION])
    directory = parser.input
    outfile = parser.output
    outdir = parser.directory
    paths = []
    for dirname, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.abspath(os.path.join(dirname, filename)))

    avg_image(paths, outfile, frames_dir=outdir)
