"""Functions related to combining the chunks."""

from rem import rem, rem_read_size
import os

base = []


def combine_chunks(is_verbose=False):
    """Combine the chunks according to their number."""
    src, des = rem('grab')
    number = check_and_pass() + 1

    if is_verbose:
        print("%d number of chunks in total..", number)

    dest = des
    des = os.path.dirname(des)
    path_tmplt = os.path.join(des, 'cpf_temp', 'cpf_temp_{}')
    i = 1
    read_size = rem_read_size('grab')
    while True:
        i += 1
        if i == number:
            break
        file = path_tmplt.format(i)

        READ_stream = open(file, 'rb')
        CONTENT = READ_stream.read(read_size)  # 52428800)  # 209715200)
        append_file(base[0], CONTENT)

        if is_verbose:
            print("%d chunk added.", i)

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
