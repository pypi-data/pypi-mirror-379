__version__ = '1.0.0.dev40'

try:
    from importlib.metadata import version
    __version__ = version("solidkit")
except:
    pass
