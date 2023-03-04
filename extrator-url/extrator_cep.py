endereco ='rua das flores 72 , apartamento 1002, rio de janeiro, rj, 23440120'

import re

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)

#[http]?[s]?[www]?