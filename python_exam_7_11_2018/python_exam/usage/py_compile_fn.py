import py_compile

import usage

py_compile.compile('py_compile_fn.py')

import importlib
importlib.reload(usage)

import sys

if __name__ == "__main__":
    print(sys.argv[0])
