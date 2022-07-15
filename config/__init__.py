import sys

from config.__config import Config


def __get_config():
    args = sys.argv[1:]
    profile = "default"
    if len(args) > 0:
        profile = args[0]
    conf = Config(profile)
    return conf


env = __get_config()
