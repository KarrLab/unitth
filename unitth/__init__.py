import pkg_resources

with open(pkg_resources.resource_filename('unitth', 'VERSION'), 'r') as file:
    __version__ = file.read().strip()
# :obj:`str`: version

# API
from .core import UnitTH
