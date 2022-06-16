from string import ascii_lowercase


def encripta(frase: str, rotation: int = 13):
    """Encript o texto."""
    encriptado = ''
    for letra in frase:
        letra = letra.lower()
        if letra == ' ':
            encriptado += letra
        elif letra not in ascii_lowercase:
            ...
        else:
            pos = ascii_lowercase.find(letra) + rotation
            letra = ascii_lowercase[pos % 26]
            encriptado += letra
    return encriptado


def decripta(frase: str, rotation: int = 13):
    """Dencript o texto."""
    dencriptado = ''
    for letra in frase:
        letra = letra.lower()
        if letra == ' ':
            dencriptado += letra
        elif letra not in ascii_lowercase:
            ...
        else:
            pos = ascii_lowercase.find(letra) - rotation
            letra = ascii_lowercase[pos % 26]
            dencriptado += letra
    return dencriptado


if __name__ == '__main__':
    print('')
