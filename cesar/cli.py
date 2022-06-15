from cesar import encripta, descripta
from argparse import ArgumentParser

parser = ArgumentParser(description='Cifra de Cesar')
parser.add_argument('frase', help='Frase a ser encriptada/descriptada', type=str)
parser.add_argument('-n', help='Valor de rotação', default=13, type=int, required=False)
parser.add_argument('-d', help='Descripta', required=False, action='store_true')

def cli():
    args = parser.parse_args()
    if args.d:
        resultado = descripta(args.frase, args.n)
    else:
        resultado = descripta(args.frase, args.n)
    
    print(f'Entrada: {args.frase}')
    print(f'Saída: {resultado}')

cli()