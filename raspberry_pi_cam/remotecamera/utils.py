
import socket


def get_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    my_ip = s.getsockname()[0]
    s.close()
    return my_ip



import sys
def signal_handler_ctrlc(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)


def get_time_micros():
    import time
    return time.time() * 1000000


def get_time_millis():
    posix_timestamp_micros = get_time_micros()
    posix_timestamp_millis = posix_timestamp_micros // 1000  # or `/ 1e3` for float
    return posix_timestamp_millis