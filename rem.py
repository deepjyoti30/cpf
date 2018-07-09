"""Remember the src and destinaton."""

loc = []
tmp_dir = []


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
