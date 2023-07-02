from utils.arguments import *

parser = Parser()
if parser.verificar_url():
    print('url valida')
else:
    print('url invalida')