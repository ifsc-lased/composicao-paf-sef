def get_xmotivo(k, l=False):
    labels = {}
    labels[-1] = '-'
    labels[100] = 'Autorizado para uso'
    labels[937] = 'Sem o fragmento DAF'
    labels[999] = 'Erro não catalogado'
    labels[245] = 'CNPJ Emitente não cadastrado'

    if labels[k] is not None:
        if l and k != -1:
            return str(k) + ' - ' + labels[k]
        else:
            return labels[k]
    return '-'


def get_resultado_sef(k, l=False):
    labels = {}
    labels[-1] = '-'
    labels[1000] = "Solicitação recebida com sucesso"
    labels[1001] = "Dispositivo registrado com sucesso"
    labels[1002] = "Registro de dispositivo removido"
    labels[1003] = "Consulta de Software Basico efetuada com sucesso"
    labels[1004] = "Notificacao de extravio efetuada com sucesso"
    labels[1005] = "Validacao do fragmento DAF realizada com sucesso"
    labels[1006] = "Modo de operação alterado com sucesso"
    labels[2000] = "registro do idDaf não encontrado"
    labels[2001] = "idpaf não corresponde ao registro do DAF"
    labels[2002] = "nonce não corresponde ao informado pela SEF"
    labels[2003] = "valor do mcounter inválido"
    labels[2004] = "assinatura de token inválida"
    labels[2005] = "CNPJ do contribuinte diverge do CNPJ da assinatura"
    labels[2006] = "idpaf não registrado"
    labels[2007] = "DAF extraviado"
    labels[2008] = "idDaf do token não corresponde ao IdDAF informado"
    labels[2009] = "DAF em situação irregular"
    labels[2010] = "justificativa inválida. A justificativa deve conter entre 15 e 255 caracteres"
    labels[2011] = "consumo indevido pelo aplicativo da empresa. Permitido no máximo 40 requisições por hora"
    labels[2012] = "CNPJ do fabricante DAF inválido"
    labels[2013] = "modelo DAF inválido"
    labels[2100] = "hash do idpaf diverge do calculado"
    labels[2101] = "assinatura gerada pela attestationkey não corresponde a um modelo de DAF certificado"
    labels[2102] = "CNPJ do responsável técnico inválido"
    labels[2103] = "identificador do CSRT (tag:idCSRT) não cadastrado na SEF"
    labels[2104] = "identificador do CSRT (tag:idCSRT) revogado"
    labels[2105] = "CNPJ do contribuinte não cadastrado"
    labels[2108] = "CNPJ do responsável técnico não cadastrado"
    labels[2300] = "IdDAF do requerente não corresponde ao IdDAF de autorização do DFe"
    labels[2301] = "chave DFe não encontrada"
    labels[2302] = "DAF deve atualizar a versão do software básico"
    labels[2303] = "versão do software básico do DAF está desatualizada"
    labels[2304] = "token de autorização inválido"
    labels[2400] = "remoção extraordinária de autorização retida indisponível para o contribuinte"
    labels[2401] = "número de recibo não encontrado"
    labels[2402] = "lote em processamento"
    labels[2403] = "a rejeição informada para o DF-e é inválida"
    labels[2404] = "as informações essenciais do DF-e são inválidas"
    labels[2500] = "notificação de extravio do DAF já foi realizada"
    labels[2600] = "o modo de operação já informado anteriormente"
    labels[9999] = "Erro não catalogado"

    if labels[k] is not None:
        if l and k != -1:
            return str(k) + ' - ' + labels[k]
        else:
            return labels[k]
    return '-'


def get_tpemis(k):
    labels = {}
    labels[-1] = '-'
    labels[1] = 'Normal'
    labels[9] = 'Off-line'
    if labels[k] is not None:
        return labels[k]
    return '-'


def get_amb(k):
    labels = {}
    labels[-1] = '-'
    labels[1] = 'Produção'
    labels[2] = 'Homolog.'
    if labels[k] is not None:
        return labels[k]
    return '-'


def get_sit(k):
    labels = {}
    labels[-1] = '-'
    labels[0] = 'Não enviada'
    labels[1] = 'Autorizada'
    labels[2] = 'Denegada'
    labels[3] = 'Cancelada'
    labels[4] = 'Rejeitada'
    if labels[k] is not None:
        return labels[k]
    return '-'


def get_res_daf(k):
    labels = {}
    labels[-1] = 'Não foi possível comunicar com o DAF - timeout'
    labels[0] = "Sucesso no processamento do pedido"
    labels[1] = "DAF em estado incorreto"
    labels[2] = "Pedido formado de forma inadequada"
    labels[3] = "Assinatura SEF inválida"
    labels[4] = "PAF não reconhecido pelo DAF"
    labels[5] = "DAF não reconhece o HMAC recebido"
    labels[6] = "Autorização não encontrada na MT do DAF"
    labels[7] = "DAF com autorizações retidas"
    labels[8] = "Versão do SB inferior ou igual à versão existente"
    labels[9] = "Modelo de DAF do SB candidato é diferente do modelo do DAF em questão"
    if labels[k] is not None:
        return labels[k]
    return '-'


def get_situacao_daf(k):
    labels = {}
    labels[-1] = '-'
    labels[0] = 'Sem registro'
    labels[1] = 'Registrado'
    labels[2] = 'Extraviado'
    labels[3] = 'ATUALIZAR SB'
    labels[4] = 'Registro irregular'
    labels[5] = 'Divergências no registro'
    labels[6] = 'Bloqueado'
    if labels[k] is not None:
        return labels[k]
    return '-'


def get_fabricante_nome(k):
    labels = {}
    labels['-1'] = '-'
    labels['86096781000185'] = 'DAF-IFSC'
    if labels[k] is not None:
        return labels[k]
    return '-'


def get_modo_operacao(k):
    labels = {}
    labels[-1] = '-'
    labels[0] = 'Dedicado'
    labels[1] = 'Compartilhado'
    if labels[k] is not None:
        return labels[k]
    return '-'
