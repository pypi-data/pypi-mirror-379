import pyaudio


def get_input_device_index_by_name(p: pyaudio.PyAudio, name: str | None = None) -> int:
    info = p.get_host_api_info_by_index(0)
    device_count = info.get("deviceCount")
    if isinstance(device_count, int):
        for i in range(0, device_count):
            device_info = p.get_device_info_by_host_api_device_index(0, i)
            if name is None:
                device_name = None
            else:
                device_name = device_info.get("name")
            if isinstance(device_name, str) or device_name is None:
                input_channels = device_info.get("maxInputChannels")
                if name == device_name and isinstance(input_channels, int) and input_channels > 0:
                    return i

    raise ValueError(f"Could not find {name}")


def get_input_devices(p: pyaudio.PyAudio) -> list[str]:
    names = []
    info = p.get_host_api_info_by_index(0)
    device_count = info.get("deviceCount")
    if isinstance(device_count, int):
        for i in range(0, device_count):
            device_info = p.get_device_info_by_host_api_device_index(0, i)
            device_name = device_info.get("name")
            if isinstance(device_name, str):
                input_channels = device_info.get("maxInputChannels")
                if isinstance(input_channels, int) and input_channels > 0:
                    names.append(device_name)

    return names


def get_default_input_device(p: pyaudio.PyAudio) -> str:
    info = p.get_host_api_info_by_index(0)
    device_count = info.get("deviceCount")
    if isinstance(device_count, int):
        for i in range(0, device_count):
            device_info = p.get_device_info_by_host_api_device_index(0, i)
            device_name = device_info.get("name")
            if isinstance(device_name, str):
                input_channels = device_info.get("maxInputChannels")
                if isinstance(input_channels, int) and input_channels > 0:
                    return device_name

    raise ValueError("No input audio devices found")
