from functools import lru_cache
from pathlib import Path

from ..datatypes import AudioT


def get_next_noise(audio: AudioT, offset: int, length: int) -> AudioT:
    """Get the next sequence of noise data from noise audio

    :param audio: Overall noise audio (entire file's worth of data)
    :param offset: Starting sample
    :param length: Number of samples to get
    :return: Sequence of noise audio data
    """
    import numpy as np

    return np.take(audio, range(offset, offset + length), mode="wrap")


def get_duration(audio: AudioT) -> float:
    """Get duration of audio in seconds

    :param audio: Time domain data [samples]
    :return: Duration of audio in seconds
    """
    from ..constants import SAMPLE_RATE

    return len(audio) / SAMPLE_RATE


def validate_input_file(input_filepath: str | Path) -> None:
    from os.path import exists
    from os.path import splitext

    from soundfile import available_formats

    if not exists(input_filepath):
        raise OSError(f"input_filepath {input_filepath} does not exist.")

    ext = splitext(input_filepath)[1][1:].lower()
    read_formats = [item.lower() for item in available_formats()]
    if ext not in read_formats:
        raise OSError(f"This installation cannot process .{ext} files")


def get_sample_rate(name: str | Path, use_cache: bool = True) -> int:
    """Get the sample rate from an audio file

    :param name: File name
    :param use_cache: If true, use LRU caching
    :return: Sample rate
    """
    if use_cache:
        return _get_sample_rate(name)
    return _get_sample_rate.__wrapped__(name)


@lru_cache
def _get_sample_rate(name: str | Path) -> int:
    """Get the sample rate from an audio file

    :param name: File name
    :return: Sample rate
    """
    import soundfile
    from pydub import AudioSegment

    from ..utils.tokenized_shell_vars import tokenized_expand

    expanded_name, _ = tokenized_expand(name)

    try:
        if expanded_name.endswith(".mp3"):
            return AudioSegment.from_mp3(expanded_name).frame_rate

        if expanded_name.endswith(".m4a"):
            return AudioSegment.from_file(expanded_name).frame_rate

        return soundfile.info(expanded_name).samplerate
    except Exception as e:
        if name != expanded_name:
            raise OSError(f"Error reading {name} (expanded: {expanded_name}): {e}") from e
        else:
            raise OSError(f"Error reading {name}: {e}") from e


def raw_read_audio(name: str | Path) -> tuple[AudioT, int]:
    from pyaaware.rs import raw_read_audio

    from ..utils.tokenized_shell_vars import tokenized_expand

    expanded_name, _ = tokenized_expand(name)

    return raw_read_audio(expanded_name)


def read_audio(name: str | Path, use_cache: bool = True) -> AudioT:
    """Read audio data from a file

    :param name: File name
    :param use_cache: If true, use LRU caching
    :return: Array of time domain audio data
    """
    if use_cache:
        return _read_audio(name)
    return _read_audio.__wrapped__(name)


@lru_cache
def _read_audio(name: str | Path) -> AudioT:
    """Read audio data from a file using soundfile

    :param name: File name
    :return: Array of time domain audio data
    """
    from pyaaware.rs import read_audio

    from ..constants import RESAMPLE_MODE
    from ..constants import SAMPLE_RATE
    from ..utils.tokenized_shell_vars import tokenized_expand

    expanded_name, _ = tokenized_expand(name)

    return read_audio(expanded_name, SAMPLE_RATE, RESAMPLE_MODE)


def get_num_samples(name: str | Path, use_cache: bool = True) -> int:
    """Get the number of samples resampled to the SonusAI sample rate in the given file

    :param name: File name
    :param use_cache: If true, use LRU caching
    :return: number of samples in resampled audio
    """
    if use_cache:
        return _get_num_samples(name)
    return _get_num_samples.__wrapped__(name)


@lru_cache
def _get_num_samples(name: str | Path) -> int:
    """Get the number of samples resampled to the SonusAI sample rate in the given file

    :param name: File name
    :return: number of samples in resampled audio
    """
    import math

    import soundfile
    from pydub import AudioSegment

    from ..constants import SAMPLE_RATE
    from ..utils.tokenized_shell_vars import tokenized_expand

    expanded_name, _ = tokenized_expand(name)

    if expanded_name.endswith(".mp3"):
        sound = AudioSegment.from_mp3(expanded_name)
        samples = sound.frame_count()
        sample_rate = sound.frame_rate
    elif expanded_name.endswith(".m4a"):
        sound = AudioSegment.from_file(expanded_name)
        samples = sound.frame_count()
        sample_rate = sound.frame_rate
    else:
        info = soundfile.info(expanded_name)
        samples = info.frames
        sample_rate = info.samplerate

    return math.ceil(SAMPLE_RATE * samples / sample_rate)
