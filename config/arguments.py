import argparse
from urllib.parse import urlparse

class parser:
    def __init__(self):
        argument = argparse.ArgumentParser()
        argument.add_argument('--url', type=str, help="aplicação web a ser explorada")
        argument.add_argument('--wordlist', type=str, help="caminho da wordlist")
        argument_parser = argument.parse_args()
        print(f'url: {argument_parser.url}')
        print(f'wordlist: {argument_parser.wordlist}')
        parsed_url = urlparse(argument_parser.url)
        def verificar_url(url):
            parsed = urlparse(url)
            if parsed.scheme in ['http', 'https'] and parsed.netloc:
                print('url valido')
            else:
                print('url invalido')
        verificar_url(argument_parser.url)

parser()
