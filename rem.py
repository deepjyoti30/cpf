"""Remember the src and destinaton."""

loc = []
tmp_dir = []
total_size = []
chunk_size = []
t_size = []


def rem(state, src=' ', des=' '):
    """If state is register than add src and dest to loc."""
    if state == 'register':
        loc.append(src)
        loc.append(des)
        return True

    if state == 'unregister':
        temp_src = loc[0]
        temp_des = loc[1]

        loc.remove(temp_src)
        loc.remove(temp_des)

        return True

    if state == 'grab':
        return(loc[0], loc[1])


def rem_dir(state, dir=''):
    """Remeber the tmp_dir."""
    if state == 'register':
        tmp_dir.append(dir)
        return True

    if state == 'unregister':
        tmp_dir.remove(tmp_dir[0])
        return True

    if state == 'grab':
        return tmp_dir[0]


def rem_size(state, size=''):
    """Remember the size of file for progress."""
    if state == 'register':
        total_size.append(size)
        return True

    if state == 'unregister':
        total_size.remove(size[0])
        return False

    if state == 'grab':
        return total_size[0]


def rem_read_size(state, chunk=0):
    """Remember the read size."""
    if state == 'register':
        chunk_size.append(chunk)
        return True

    if state == 'unregister':
        chunk_size.remove(chunk_size[0])
        return True

    if state == 'grab':
        return chunk_size[0]
