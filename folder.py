"""Folder related funstions are defined here."""

import os
import cpf
from rem import rem
import threading


class folder(threading.Thread):
    """Class to use threading for folder copy."""

    def __init__(self, src, des, is_verbose):
        """Init the stuff."""
        threading.Thread.__init__(self)
        self.src = src
        self.des = des
        self.is_verbose = is_verbose

    def run(self):
        """Run the function."""
        cpf.do(self.src, self.des, self.is_verbose)


def check_existence(src):
    """Check if the src is a valid folder."""
    if not os.path.isdir(src):
        print("{}: not a directory.".format(src))
        return False

    return True


def create_des(des):
    """Create the des folder."""
    if not os.path.isdir(des):
        os.mkdir(des)

    return True


def scan_pass(src, des, is_verbose=False):
    """Scan the src folder and pass all files to be copied."""
    for file in os.listdir(src):
        sec_src = os.path.join(src, file)
        sec_des = os.path.join(des, file)

        # Check if sec_src is a folder.
        # If it is then pass it to
        if not os.path.isdir(sec_src):
            # Register the src and des
            rem('register', sec_src, sec_des)

            cpf.do(sec_src, sec_des, is_verbose)
        else:
            cpf.run_recursive(sec_src, sec_des, is_verbose)
