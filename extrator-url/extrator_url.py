import re

class ExtratorURL:
    def __init__(self , url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if self.url == '':
            raise ValueError('a url está vazia')

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('a url não é válida')

    def get_url_base(self):
        indice = self.url.find('?')
        url_base = self.url[:indice]
        return url_base

    def get_url_parametros(self):
        indice = self.url.find('?')
        url_parametros = self.url[indice + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_param = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_param + len(parametro_busca) + 1
        indice_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor: indice_comercial]

        return valor

    def converter(self):
        moeda_origem = self.get_valor_parametro("moedaOrigem")
        quantidade= int(self.get_valor_parametro("quantidade"))
        #qunatidade = int

        if moeda_origem == 'dolar':
            convetido = quantidade * 5.5
        if moeda_origem == 'real':
            convetido = quantidade / 5.5

        return convetido


    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url

    def __eq__(self, other):
        return self.url == other.url


extrator = ExtratorURL("bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100")

