"""Functions used to show progress are defined here."""

import threading
from rem import rem, rem_size, rem_read_size
import os
from time import sleep
import sys


class progress(threading.Thread):
    """Keep the progress bar running in another thread."""

    def __init__(self, which):
        """Init the stuff."""
        threading.Thread.__init__(self)
        self.which = which

    def run(self):
        """Run the thread."""
        if self.which == 'copy':
            show_progress_copy()
        elif self.which == 'chunk':
            show_progress_chunk()


def show_progress_copy():
    """Show progress by printing recursively."""
    src, des = rem('grab')
    des_dir = os.path.dirname(des)
    tmp_dir = os.path.join(des_dir, 'cpf_temp')
    path_to_tmp = os.path.join(des_dir, 'cpf_temp', 'cpf_temp_1')

    count = len(os.listdir(tmp_dir))

    try:
        total_size = rem_size('grab')
        part = total_size/count
        i = 5
        last = part

        for i in range(20):
            while True:
                part = os.path.getsize(path_to_tmp)
                if part > last:
                    last = part
                    break
                else:
                    sleep(0.2)

            sys.stdout.write('\r')
            sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
            sys.stdout.flush()

        print('')

    except Exception:
        print('Something went wrong while showing the progress bar.\a')
        pass


def calculate_pieces():
    """Calculate the number of chunks."""
    chunk_size = rem_read_size('grab')
    total_size = rem_size('grab')

    pieces = int(total_size/chunk_size)
    rem_piece = total_size % chunk_size

    if rem_piece != 0:
        pieces += 1

    return pieces


def show_progress_chunk():
    """Show the progress of making chunks."""
    src, des = rem('grab')
    des_dir = os.path.dirname(des)
    tmp_dir = os.path.join(des_dir, 'cpf_temp')

    number_chunks = calculate_pieces()

    try:
        last = len(os.listdir(tmp_dir))

        for i in range(20):
            while True:
                pieces_tillnow = len(os.listdir(tmp_dir))
                if pieces_tillnow == number_chunks:
                    # If the porgressbar isn not complete
                    if i < 20:
                        i = 20
                        break
                    # Else exit the loop
                    else:
                        sys.stdout.flush()
                        print('')
                        return True
                elif pieces_tillnow > last:
                    last = pieces_tillnow
                    break
                else:
                    sleep(0.2)

            sys.stdout.write('\r')
            sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
            sys.stdout.flush()

        print('')
    except Exception:
        print('Something went wrong while showing the progress bar.\a')
        pass
