import random
import re

from app.models.municipio import Municipio




def gera_nome_max(qnt):
    prm = 'RTPLKJGFDSZCVBNM'
    vgl = 'aeiou'
    mei = 'aeiouyhqwrtplkjhgfdzxcvbnm'

    nome = random.choice(prm)
    for l in range(0, qnt - 1):
        if l % 2 != 0:
            nome = nome + random.choice(mei)
        else:
            nome = nome + random.choice(vgl)
    return nome


def gerar_nome(qntPalavra, qntLetras=0):
    prm = 'RTPLKJGFDSZCVBNM'
    vgl = 'aeiou'
    mei = 'aeiouyhqwrtplkjhgfdzxcvbnm'

    nome = random.choice(prm)
    for p in range(0, qntPalavra):
        for l in range(0, random.randint(3, 8)):
            if l % 2 != 0:
                nome = nome + random.choice(mei)
            else:
                nome = nome + random.choice(vgl)
        nome = nome + ' '

    return nome[0:-1]


def gerar_telefone():
    tel = '(48) 9'
    for i in range(0, 2):
        tel = tel + str(random.randint(7, 9))
    for i in range(0, 2):
        tel = tel + str(random.randint(0, 9))
    tel = tel + '-'
    for i in range(0, 4):
        tel = tel + str(random.randint(0, 9))
    return tel


def gerar_csc():
    letras = 'QWERTYUIOPLKJHGFDSAZXCVBNM0123456789'

    csc = ''
    for p in range(0, 36):
        csc = csc + random.choice(letras)

    return csc


def gerar_email(nome):
    return 'contato@' + re.sub(" ", "", nome)[0:6].lower() + '.com.br'


def gerar_endereco():
    logradouros = ['Aeroporto', 'Alameda', 'Área', 'Avenida', 'Campo', 'Chácara', 'Colônia', 'Condomínio', 'Conjunto',
                   'Distrito', 'Esplanada', 'Estação', 'Estrada', 'Favela', 'Fazenda', 'Feira', 'Jardim', 'Ladeira',
                   'Lago', 'Lagoa', 'Largo', 'Loteamento', 'Morro', 'Núcleo', 'Parque', 'Passarela', 'Pátio', 'Praça',
                   'Quadra', 'Recanto', 'Residencial', 'Rodovia', 'Rua', 'Setor', 'Sítio', 'Travessa', 'Trecho',
                   'Trevo', 'Vale', 'Vereda', 'Via', 'Viaduto', 'Viela', 'Vila']
    municipios = Municipio.query.all()
    municipio = municipios[random.randint(0, len(municipios))]
    end = {"endereco": gerar_nome(2), "cep": random.randint(10000000, 99999999), "bairro": gerar_nome(1),
           "complemento": 'Sala ' + str(random.randint(100, 555)), "logradouro": random.choice(logradouros),
           "numero": random.randint(2, 999), "municipio": municipio}

    return end
