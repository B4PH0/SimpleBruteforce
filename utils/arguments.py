import argparse
from urllib.parse import urlparse

class Parser:
    def __init__(self):
        argument = argparse.ArgumentParser()
        argument.add_argument('--url', type=str, help="aplicação web a ser explorada")
        argument.add_argument('--wordlist', type=str, help="caminho da wordlist")
        self.argument_parser = argument.parse_args()

    def verificar_url(self):
        parsed = urlparse(self.argument_parser.url)
        if parsed.scheme in ['http', 'https'] and parsed.netloc:
            return True
        else:
            return False
