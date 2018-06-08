from io_utils import IOParser
from ia_helper import avg_image, DIR_OPTION
import os

import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile
import math

from random import randint

def get_audio_files(directory):
    files = []
    for dirname, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if '.wav' in filename:
                files.append(os.path.abspath(os.path.join(dirname, filename)))
    return files


def avg_audio(paths, out, duration):
    shortest = math.inf
    wavfiles = []
    rate = None
    for path in paths:
        fs, data = wavfile.read(path)
        rate = fs
        track = data.T[0]
        size = len(track)
        shortest = size if size < shortest else shortest
        wavfiles.append(track)

    num_tracks = len(wavfiles)
    chunk = rate * duration
    avg = np.zeros(chunk)
    for track in wavfiles:
        index = randint(0, shortest - chunk)
        track = track[index:index+chunk]
        avg = avg + track / num_tracks

    wavfile.write(out, rate, avg)

DURATION = {
    'short': '-d',
    'verbose': '--duration',
    'help': 'length of the output in seconds',
    'required': False,
    'type': int
}

if __name__ == '__main__':
    parser = IOParser(add_args=[DURATION])
    input = parser.input
    output = parser.output
    duration = parser.duration

    wavs = get_audio_files(input)
    avg_audio(wavs, output, duration)
