"""cpf - cp faster.

* A utility that would work like cp
* but fasterself.
* It first breaks the file into chunks
* Then uses multiple threads to copy those file
* chunks at the same time.
* Then it combines the filechunks.
"""

import argparse
import sep
from rem import rem, rem_dir
import os
import combine
import time
from shutil import rmtree
import cleanup


def arguments():
    """Parse the arguments."""
    parser = argparse.ArgumentParser()

    parser.add_argument('SRC', help="Source File Name.",
                        type=str)
    parser.add_argument('DES', help="Destinaion File Name.",
                        type=str)
    parser.add_argument('-v', '--verbose',
                        help="Explain what is being done.",
                        action='store_true')

    args = parser.parse_args()

    return args


def main():
    """Run on program call."""
    args = arguments()

    # Extract the source and destinaton
    src = args.SRC
    des = args.DES
    is_verbose = args.verbose

    # Check src and des
    if not sep.check_existence(src, des):
        exit(1)
    else:
        # Register the src and des
        rem('register', src, des)

    if is_verbose:
        print("{} -> {}".format(src, des))

    # Make a temp folder to keep the files
    tmp_dir = os.path.join(os.path.dirname(des), 'cpf_temp')

    if is_verbose:
        print("Making temp directory..")
    os.mkdir(tmp_dir)
    rem_dir('register', tmp_dir)

    beg_time = time.time()
    # Start breaking into chunks

    if is_verbose:
        print("Making chunks...")

    sep.make_chunks(is_verbose)

    if is_verbose:
        print("Combining chunks..")

    # Now combine the stuff
    combine.combine_chunks()

    # Show copy time
    print(str(round(time.time() - beg_time)) + ' seconds.')

    # Remove the folder
    if is_verbose:
        print('Cleaning up...')

    cleanup.pass_names(tmp_dir)
    rmtree(tmp_dir)

    rem('unregister')
    rem_dir('unregister')


main()
