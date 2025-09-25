from .base import ViewersEnum, ViewerError

from .viewer0D import Viewer0D
from .viewer1D import Viewer1D
from .viewer2D import Viewer2D
from .viewerND import ViewerND
from .viewer import ViewerDispatcher


DATA_TYPES = ['Data0D', 'Data1D', 'Data2D', 'DataND']
