print("__name__={}__file__={}".format(__name__,__file__))
from sub_package1 import *
from sub_package1.sub_sub_package1 import *
from sub_package2 import *
from sub_package2.sub_sub_package2 import *
from sub_package2.sub_sub_package2 import module1 as x
x.fn1()
from sub_package2 import module2 as y
y.fn1()
"""
For efficiency reasons, each module is only imported once per interpreter session.
Therefore, if you change your modules, you must restart the interpreter – or,
if it’s just one module you want to test interactively,
use importlib.reload(), e.g. import importlib; importlib.reload(modulename).
"""
"""
You can also write relative imports, with the from module import name form of import statement.
These imports use leading dots to indicate the current and parent packages involved in the relative import.
From the surround module for example, you might use:

from . import echo
from .. import formats
from ..filters import equalizer

"""
