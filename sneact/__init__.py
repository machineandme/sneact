from sneact._conditions import When as when
from sneact._conditions import WhenNot as when_not
from sneact._magic_tags import MagicHTMLTag
from sneact._scopes import _SneactScope
from sneact._sneact import Sneact

__version__ = "0.0.6"

_ = MagicHTMLTag("\n")
then = MagicHTMLTag("")
s = _SneactScope()
