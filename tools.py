def sizeof(p_int):
    size = p_int
    if size >= 1024 * 1024 * 1024:
        size = '%.2fGB' % (size / 1024 / 1024 / 1024)
    elif size >= 1024 * 1024:
        size = '%.2fMB' % (size / 1024 / 1024)
    elif size >= 1024:
        size = '%.2fKB' % (size / 1024)
    else:
        size = str(size) + 'B'
    return size
