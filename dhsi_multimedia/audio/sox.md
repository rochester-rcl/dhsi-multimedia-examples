## Sox Example Commands

#### 1. Converting Files
Basic conversion
```
sox /path/to/audio.wav /path/to/audio.mp3
```
Setting the sample rate (48kHz)
```
sox -r 48000 /path/to/audio.wav /path/to/audio.mp3
```
Convert stereo to mono
```
sox -c 1 /path/to/audio.wav /path/to/audio.mp3
```

#### 2. Manipulating Files
Increase the volume of a file (2x louder)
```
sox -v 2.0 /path/to/audio.wav /path/to/audio.mp3
```
Decrease the volume of a file (2x quieter)
```
sox -v -0.5 /path/to/audio.wav /path/to/audio.mp3
```
Trim a file (trims a 30 second clip from the beginning of a file )
```
sox /path/to/audio.wav /path/to/audio.mp3 trim 0 30
```
Reverse an audio file
```
sox /path/to/audio.wav /path/to/audio.mp3 reverse
```
Speed up an audio file (2x faster)
```
sox /path/to/audio.wav /path/to/audio.mp3 speed 2.0
```
Speed up an audio file (2x slower)
```
sox /path/to/audio.wav /path/to/audio.mp3 speed 0.5
```

#### 3. Audio Filtering and Effects
Apply a low pass filter (everything below this frequency "passes" through)
```
sox /path/to/audio.wav /path/to/audio.mp3 lowpass 500
```
Apply a high pass filter (everything above this frequency "passes" through)
```
sox /path/to/audio.wav /path/to/audio.mp3 highpass 500
```
Sox has several effects you can apply (chorus, flanger, echo). The syntax is like this:
```
sox /path/to/audio.wav /path/to/audio.mp3 [EFFECT NAME] [EFFECT PARAMETERS]
```
You can find them here: http://sox.sourceforge.net/sox.html

#### 4. Analysis
Get some technical metadata on the file
```
sox --i /path/to/audio.wav
```
Produce a spectrogram of your file
```
sox /path/to/audio.wav -n spectrogram -o /path/to/image.png
```
