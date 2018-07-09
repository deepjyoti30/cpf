"""File disassembling related functions.

* All functions related to breaking the file
* into chunks in order to copy them are
* defined here.
"""

import os
from print import PREPEND
from rem import rem
import copy


def make_chunks():
    """Make chunks of the file passed."""
    src, des = rem('grab')

    # Open the file in binary
    FILE_STREAM = open(src, 'rb')

    count = 0
    while True:
        READ_CHUNK = FILE_STREAM.read(104857600)  # 52428800)  # 209715200)
        count += 1

        if not READ_CHUNK:
            return True

        copy.copy_chunks(READ_CHUNK, count)


def check_existence(src, dest):
    """Check if the source exists and destinaton does not."""
    if not os.path.isfile(src):
        # Show that source doesn't exist
        PREPEND(2)
        print("{}: No such file\a".format(src))
        return False

    if os.path.isfile(dest):
        # Show that destinaton already exists
        PREPEND(2)
        print("{}: already exists\a".format(dest))
        return False

    return True
