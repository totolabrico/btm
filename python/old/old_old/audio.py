

from pydub import AudioSegment
from pydub.playback import play
# Download an audio file
#urllib.request.urlretrieve("https://tinyurl.com/wx9amev", "metallic-drums.wav")
# Load into PyDub
loop = AudioSegment.from_wav("/home/pi/Bureau/btm_1/python/1_kick.wav")
# Play the result

def playSample():
    play(loop)
    return

'''

from pydub import AudioSegment
sound1 = AudioSegment.from_file("/path/to/sound.wav", format="wav")
sound2 = AudioSegment.from_file("/path/to/another_sound.wav", format="wav")

# sound1 6 dB louder, then 3.5 dB quieter
louder = sound1 + 6
quieter = sound1 - 3.5

# sound1, with sound2 appended
combined = sound1 + sound2

# sound1 repeated 3 times
repeated = sound1 * 3

# duration
duration_in_milliseconds = len(sound1)

# first 5 seconds of sound1
beginning = sound1[:5000]

# last 5 seconds of sound1
end = sound1[-5000:]

# split sound1 in 5-second slices
slices = sound1[::5000]

# Advanced usage, if you have raw audio data:
sound = AudioSegment(
    # raw audio data (bytes)
    data=b'…',

    # 2 byte (16 bit) samples
    sample_width=2,

    # 44.1 kHz frame rate
    frame_rate=44100,

    # stereo
    channels=2
)
'''
