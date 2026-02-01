from typing import List

def split(data: str, sep=None, maxsplit=-1):
    final = []

    if data == '':
        return final

    if maxsplit == 0:
        if sep is None:
            stripped = data.strip()
            return [stripped] if stripped else []
        else:
            return [data]

    if sep is None:
        word = ''
        splits_done = 0
        i = 0
        n = len(data)
        while i < n:
            if data[i].isspace():
                if word:
                    final.append(word)
                    word = ''
                    splits_done += 1
                    if 0 < maxsplit == splits_done:
                        rest = data[i + 1:].lstrip()
                        if rest:
                            final.append(rest)
                        return final
                while i < n and data[i].isspace():
                    i += 1
                continue
            else:
                word += data[i]
            i += 1
        if word:
            final.append(word)
        return final

    else:
        i = 0
        n = len(data)
        sep_len = len(sep)
        splits_done = 0
        start = 0

        while i <= n - sep_len:
            if maxsplit != -1 and splits_done >= maxsplit:
                break
            if data[i:i + sep_len] == sep:
                final.append(data[start:i])
                splits_done += 1
                i += sep_len
                start = i
            else:
                i += 1
        final.append(data[start:])
        return final




if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']


split('    Hi     Python    world!')
