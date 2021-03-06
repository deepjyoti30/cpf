"""Funtions related to copying the chunks."""

import threading
import os
from rem import rem_dir, rem


class copy(threading.Thread):
    """Class to use multithreading for copying."""

    def __init__(self, chunk, token):
        """Init the passed arguments for threads."""
        threading.Thread.__init__(self)
        self.chunk = chunk
        self.token = token

    def run(self):
        """Run the copy_chunks function."""
        write_chunk(self.chunk, self.token)


def write_chunk(chunk, token):
    """Write the small chunks."""
    dest = rem_dir('grab')
    # input(dest)
    file_name = '{}_{}'.format('cpf_temp', token)
    dest_file_name = os.path.join(os.path.abspath(dest), file_name)
    # input(dest_file_name)
    WRITE_STREAM = open(dest_file_name, 'wb')
    WRITE_STREAM.write(chunk)
    WRITE_STREAM.close()

    return True


def copy_chunks(chunk, token):
    """Copy the chunks of the file to destinaton dir.

    Make a folder and keep the chunks in that folder.
    Later combine them into a single file.

    chunk: is the part of the file that would be copied.
    token: should be a number that would be used to keep track
    of the copied file.
    """
    # Open a thread to write this chunk
    thread = copy(chunk, token)
    thread.start()
    thread.join()


def simple_copy():
    """Copy the file simply by opening it in write mode in destinaton."""
    src, des = rem('grab')
    # All we need to do is keep the filename same
    # Since the file is of 0 bytes
    des_name = os.path.basename(des)
    des_dir = os.path.dirname(des)

    des = os.path.join(des_dir, des_name)

    # Now simply open and close des in write mode
    TEMP_STREAM = open(des, 'w')
    TEMP_STREAM.close()

    return True
