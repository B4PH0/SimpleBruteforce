from . import arguments
import http.client

class brute:
    def __init__(self):
        self.funcao = arguments.Parser()
    
    def bruteforce(self):
        wordlist = self.funcao.argument_parser.wordlist
        url = self.funcao.argument_parser.domain
        slash = "/"
        palavra = url.split()
        with open(wordlist, mode="r", encoding='utf-8') as arquivo:
            for line in arquivo:
                line = line.strip('\n')
                directory = slash + line
                conn = http.client.HTTPConnection(url)
                conn.request("GET", directory)
                response = conn.getresponse()
                headers = response.getheaders()
                conn2 = http.client.HTTPConnection(url)
                conn2.request("GET", directory)
                response2 = conn2.getresponse()
                if response2.status != 404:
                    print(f'{url}{directory} | {response2.status}')
            conn.close()