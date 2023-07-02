import requests
from Wappalyzer import Wappalyzer, WebPage

#response = requests.get('http://businesscorp.com.br')
#conteudo = response.text

#if "jquery" in conteudo:
#    print('roda jquery')
#else:
#    print("não roda jquery")
wappalyzer = Wappalyzer.latest()
webpage = WebPage.new_from_url('https://saotome.rn.gov.br')
resultado = wappalyzer.analyze(webpage)
if 'PHP' in resultado:
    print('A aplicação web utiliza o serviço ou framework desejado.')
else:
    print('A aplicação web não utiliza o serviço ou framework desejado.')
