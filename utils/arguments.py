import argparse

class Parser:
    def __init__(self):
        argument = argparse.ArgumentParser()
        argument.add_argument('--domain', type=str, help="aplicação web a ser explorada")
        argument.add_argument('--wordlist', type=str, help="caminho da wordlist")
        self.argument_parser = argument.parse_args()

