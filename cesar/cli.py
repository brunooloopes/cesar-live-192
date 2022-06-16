from argparse import ArgumentParser

from cesar import decripta, encripta

parser = ArgumentParser(description='Cifra de Cesar')
parser.add_argument(
    'frase', help='Frase a ser encriptada/decriptada', type=str
)
parser.add_argument(
    '-n', help='Valor de rotação', default=13, type=int, required=False
)
parser.add_argument('-d', help='Decripta', required=False, action='store_true')


def cli():
    args = parser.parse_args()
    if args.d:
        resultado = decripta(args.frase, args.n)
    else:
        resultado = encripta(args.frase, args.n)

    print(f'Entrada: {args.frase}')
    print(f'Saída: {resultado}')


cli()

if __name__ == '__main__':
    pass
