from importlib.resources import as_file
from importlib.resources import files

SAMPLE_RATE = 16000
RESAMPLE_MODE = "soxr_hq"
CHANNEL_COUNT = 1
BIT_DEPTH = 32
SAMPLE_BYTES = BIT_DEPTH // 8
FLOAT_BYTES = 4

with as_file(files("sonusai.data").joinpath("whitenoise.wav")) as path:
    DEFAULT_NOISE = str(path)

with as_file(files("sonusai.data").joinpath("speech_ma01_01.wav")) as path:
    DEFAULT_SPEECH = str(path)
