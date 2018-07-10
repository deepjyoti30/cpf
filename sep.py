"""File disassembling related functions.

* All functions related to breaking the file
* into chunks in order to copy them are
* defined here.
"""

import os
from rem import rem, rem_read_size
import copy
import progress


def make_chunks(is_verbose=False, show_progress=False):
    """Make chunks of the file passed."""
    src, des = rem('grab')

    # Open the file in binary
    FILE_STREAM = open(src, 'rb')
    rem_read_size('register', 104857600)

    # After registering show progress
    if show_progress:
        progress_bar = progress.progress('chunk')
        progress_bar.start()

    count = 0
    while True:
        read_size = rem_read_size('grab')
        READ_CHUNK = FILE_STREAM.read(read_size)  # 52428800)  # 209715200)
        count += 1

        if not READ_CHUNK:
            return True

        if is_verbose:
            print("Copying chunk: {}".format(count))

        copy.copy_chunks(READ_CHUNK, count)


def check_existence(src, dest):
    """Check if the source exists and destinaton does not."""
    if not os.path.isfile(src):
        # Show that source doesn't exist
        print("{}: No such file\a".format(src))
        return False

    if os.path.isdir(src):
        # Show that source is a folder
        print("{}: is a folder".format(src))
        return False

    if os.path.isfile(dest):
        # Show that destinaton already exists
        print("{}: already exists\a".format(dest))
        return False

    return True


def check_filesize():
    """Check the filesize.

    If the file is 0 bytes size, then no
    need to use threads and all.
    If it is not then return True.
    """
    src, des = rem('grab')
    if os.path.getsize(src) == 0:
        return False
    else:
        return True
