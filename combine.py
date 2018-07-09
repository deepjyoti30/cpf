"""Functions related to combining the chunks."""

from rem import rem
import os
import threading

base = []


class combine(threading.Thread):
    """Class to use multithreading for combining."""

    def __init__(self, base, chunk, token):
        """Init the stuff."""
        threading.Thread.__init__(self)
        self.base = base
        self.chunk = chunk
        self.token = token

    def run(self):
        """Run the threads using this function."""
        write_nana(self.base, self.chunk, self.token)


def combine_chunks():
    """Combine the chunks according to their number."""
    src, des = rem('grab')
    number = check_and_pass() + 1
    dest = des
    des = os.path.dirname(des)
    path_tmplt = os.path.join(des, 'cpf_temp', 'cpf_temp_{}')
    i = 1
    while True:
        i += 1
        if i == number:
            break
        file = path_tmplt.format(i)
        # input(file)
        READ_stream = open(file, 'rb')
        CONTENT = READ_stream.read(104857600)  # 52428800)  # 209715200)
        append_file(base[0], CONTENT)
        # write_nana(base[0], CONTENT, i)
        #  input(base[0])
        """thread = combine(base[0], CONTENT, i)
        thread.start()
        thread.join()
        """
        READ_stream.close()

    # Rename the base file to des
    os.rename(path_tmplt.format(1), dest)


def append_file(src, des):
    """Append the des to src."""
    # Open src in append mode
    APPEND_STREAM = open(src, 'ab')
    APPEND_STREAM.write(des)
    APPEND_STREAM.close()
    return True


def write_nana(base, chunk, token):
    """Just a test function."""
    count = token - 1
    btoseek = count * 104857600
    # Seek from the beginning
    APPEND_STREAM = open(base, 'rb+')
    APPEND_STREAM.seek(btoseek, 0)
    APPEND_STREAM.write(chunk)
    APPEND_STREAM.close()
    return True


def check_and_pass():
    """Check the cpf_temp folder and pass the files."""
    src, des = rem('grab')
    dest_folder = os.path.join(os.path.dirname(des), 'cpf_temp')
    count = 0
    for file in os.listdir(dest_folder):
        count += 1
        if file == 'cpf_temp_1':
            # Take this as the base and append the other files to this one
            base.append(os.path.join(dest_folder, file))

    return count
