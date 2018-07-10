"""cpf - cp faster.

* A utility that would work like cp
* but faster.
* It first breaks the file into chunks
* Then uses multiple threads to copy those file
* chunks at the same time.
* Then it combines the filechunks.
"""

import argparse
import sep
from rem import rem, rem_dir, rem_size
import os
import combine
import time
from shutil import rmtree
import cleanup
import folder
import progress
import copy

beg_time = time.time()


def arguments():
    """Parse the arguments."""
    parser = argparse.ArgumentParser()

    parser.add_argument('SRC', help="Source File Name.",
                        type=str)
    parser.add_argument('DES', help="Destinaion File Name.",
                        type=str)
    parser.add_argument('-r', '--recursive',
                        help="Copy the files recursively",
                        action='store_true')
    parser.add_argument('-p', '--progress',
                        help="Show a progress bar",
                        action='store_true')
    parser.add_argument('-v', '--verbose',
                        help="Explain what is being done",
                        action='store_true')

    args = parser.parse_args()

    return args


def run_recursive(src, des, is_verbose, show_progress):
    """Run if -r is passed."""
    if not folder.check_existence(src):
        exit(2)

    folder.create_des(des)

    folder.scan_pass(src, des, is_verbose, show_progress)


def main():
    """Run on program call."""
    args = arguments()

    # Extract the source and destinaton
    src = args.SRC
    des = args.DES
    is_verbose = args.verbose
    is_recursive = args.recursive
    show_progress = args.progress

    # If recursive is true then pass to check if folders exist
    if is_recursive:
        run_recursive(src, des, is_verbose, show_progress)
        exit(0)

    # Check src and des
    if not sep.check_existence(src, des):
        exit(1)
    else:
        # Register the src and des
        rem('register', src, des)

    do(src, des, is_verbose, show_progress)


def do(src, des, is_verbose=False, show_progress=False):
    """Copy of src to dst."""
    if is_verbose or show_progress:
        print("{} -> {}".format(src, des))

    # If the filesize is zero then use simple_copy
    if not sep.check_filesize():
        input('Simple copy')
        copy.simple_copy()
        return True

    if show_progress:
        rem_size('register', os.path.getsize(src))

    # Make a temp folder to keep the files
    tmp_dir = os.path.join(os.path.dirname(des), 'cpf_temp')

    if is_verbose:
        print("Making temp directory..")

    os.mkdir(tmp_dir)
    rem_dir('register', tmp_dir)

    # Start breaking into chunks

    if is_verbose or show_progress:
        print("Making chunks...")

    sep.make_chunks(is_verbose, show_progress)

    if is_verbose or show_progress:
        print("Combining chunks..")

    if show_progress:
        progress_bar = progress.progress('copy')
        progress_bar.start()

    # Now combine the stuff
    combine.combine_chunks()

    # Remove the folder
    if is_verbose or show_progress:
        print('Cleaning up...')

    # Wait for the progress_bar thread to end
    if show_progress:
        progress_bar.join()

    cleanup.pass_names(tmp_dir)
    try:
        rmtree(tmp_dir)
    except Exception:
        pass

    rem('unregister')
    rem_dir('unregister')


if __name__ == "__main__":
    main()


# Show copy time
print(str(round(time.time() - beg_time)) + ' seconds.')
