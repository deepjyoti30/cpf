"""Functions related to cleaning up the temp_dir."""

import threading
import os


class remove(threading.Thread):
    """Remove the temp stuff."""

    def __init__(self, file):
        """Init the stuff."""
        threading.Thread.__init__(self)
        self.file = file

    def run(self):
        """Use multiple threads."""
        remove_dir(self.file)


def remove_dir(file):
    """Remove file using shutil."""
    try:
        os.remove(file)
        return True
    except Exception:
        return False


def pass_names(folder):
    """Pass the names of files present in folder."""
    for file in os.listdir(folder):
        file = os.path.join(folder, file)
        thread = remove(file)
        thread.start()
