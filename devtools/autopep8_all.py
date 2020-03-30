"""
Run this script to run autopep8 on everything in the library
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from cleverhansl2l.devtools.list_files import list_files
from cleverhansl2l.utils import shell_call

for f in list_files(".py"):

  command = ["autopep8", "-i", "--indent-size", "2", f]
  shell_call(command)
