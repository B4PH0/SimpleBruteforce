from arguments import *
import http.client
import threading
import io

class brute:
    def __init__(self):
        self.funcao = Parser()
    
    def bruteforce(self):
        wordlist = self.funcao.argument_parser.wordlist
        url = self.funcao.argument_parser.url
        slash = "/"
        with io.open(wordlist, mode="r", encoding='utf-8') as arquivo:
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
                if response2 == 200:
                    print(f'{url}{directory} | 200 CODE')
                elif response2 == 401:
                    print(f'{url}{directory} | 401 CODE')
                else:
                    print(f'{url}{directory} | {response2.status} CODE')
            conn.close()
objeto = brute()
objeto.bruteforce()