from io_utils import IOParser
from audio import get_audio_files, avg_audio, DURATION

if __name__ == '__main__':
    parser = IOParser(add_args=[DURATION])
    input = parser.input
    output = parser.output
    duration = parser.duration

    wavs = get_audio_files(input)
    avg_audio(wavs, output, duration)
