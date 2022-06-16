from string import ascii_lowercase


def encripta(frase: str, n: int = 13):
    """encript o texto"""
    encriptado = ''
    for l in frase:
        l = l.lower()
        if l == ' ':
            encriptado += l
        elif l not in ascii_lowercase:
            ...
        else:
            pos = ascii_lowercase.find(l) + n
            l = ascii_lowercase[pos % 26]
            encriptado += l
    return encriptado


def decripta(frase: str, n: int = 13):
    """dencript o texto"""
    dencriptado = ''
    for l in frase:
        l = l.lower()
        if l == ' ':
            dencriptado += l
        elif l not in ascii_lowercase:
            ...
        else:
            pos = ascii_lowercase.find(l) - n
            l = ascii_lowercase[pos % 26]
            dencriptado += l
    return dencriptado


if __name__ == '__main__':
    pass
