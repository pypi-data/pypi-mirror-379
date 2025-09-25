def bytes_for_char_utf_8(c):
    return len(c.encode("utf-8", errors="replace"))


def split_utf8(s, maxsize=288):
    b = 0
    total = 0
    result = []
    for i, c in enumerate(s):
        cs = bytes_for_char_utf_8(c)
        total += cs
        if total > maxsize:
            result.append(s[b:i])
            total = cs
            b = i
        elif i == len(s) - 1:
            result.append(s[b:])
    return result


class ConsoleCommandExecutor:
    def __init__(self):
        pass
