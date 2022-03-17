import os

from decouple import config


def env(var_name):
    try:
        var = os.environ[var_name]
    except KeyError:
        var = config(var_name)
    return var

