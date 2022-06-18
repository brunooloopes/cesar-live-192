from shutil import which
from tempfile import NamedTemporaryFile, TemporaryDirectory, TemporaryFile
from time import sleep

# with open('.cache/text.txt', 'w+') as file:
    # file.write('testando....')

with TemporaryDirectory(dir='.cache/', prefix='dir_') as dir:
    with NamedTemporaryFile(dir=dir, prefix='permissoes_', delete=False, suffix='.txt') as file:
        file.write(b'testando....')
        file.seek(0)
        print(file.read())
        print(file.name)
        sleep(3)
