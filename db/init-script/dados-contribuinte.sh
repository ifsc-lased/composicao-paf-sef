#!/bin/bash
# 2021 LaSED - IFSC

if [  $# -ne 2 ]; then
    echo "ERRO: Arquivo com dados do contribuinte ou arquivo para saída não foi informado."
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "ERRO: Arquivo $1 não foi encontrado."
    exit 1
fi

arquivo="$1"
saida="$2"

function pop {
    grep "${1}" "$arquivo" | cut -d'=' -f2
}

cont_cnpj=$(pop 'cont_cnpj')
cont_ecnpj_nome=$(pop 'cont_ecnpj_nome')
cont_ecnpj_senha=$(pop 'cont_ecnpj_senha')
cont_inscricaoSC=$(pop 'cont_inscricaoSC')
cont_razaoSocial=$(pop 'cont_razaoSocial')
cont_nomeFantasia=$(pop 'cont_nomeFantasia')
cont_telefone=$(pop 'cont_telefone')
cont_email=$(pop 'cont_email')
cont_credenciadoNfe=$(pop 'cont_credenciadoNfe')
cont_endereco=$(pop 'cont_endereco')
cont_logradouro=$(pop 'cont_logradouro')
cont_complemento=$(pop 'cont_complemento')
cont_cep=$(pop 'cont_CEP')
cont_numero=$(pop 'cont_numero')
cont_bairro=$(pop 'cont_bairro')
cont_cidade=$(pop 'cont_cidade')
cont_idpaf=$(pop 'cont_idpaf')
cont_csc_id=$(pop 'cont_csc_id')
cont_csc_hash=$(pop 'cont_csc_hash')

certificado_sef=$(pop 'certificado_sef')

fab_paf_cnpj=$(pop 'fab_paf_cnpj')
fab_paf_inscricaoSC=$(pop 'fab_paf_inscricaoSC')
fab_paf_razaoSocial=$(pop 'fab_paf_razaoSocial')
fab_paf_nomeFantasia=$(pop 'fab_paf_nomeFantasia')
fab_paf_telefone=$(pop 'fab_paf_telefone')
fab_paf_email=$(pop 'fab_paf_email')
fab_paf_endereco=$(pop 'fab_paf_endereco')
fab_paf_logradouro=$(pop 'fab_paf_logradouro')
fab_paf_complemento=$(pop 'fab_paf_complemento')
fab_paf_cep=$(pop 'fab_paf_CEP')
fab_paf_numero=$(pop 'fab_paf_numero')
fab_paf_bairro=$(pop 'fab_paf_bairro')
fab_paf_cidade=$(pop 'fab_paf_cidade')
fab_paf_csrt_id=$(pop 'fab_paf_csrt_id')
fab_paf_csrt_hash=$(pop 'fab_paf_csrt_hash')

nome_versao_paf=$(pop 'nome_versao_paf')

fab_cnpj=$(pop 'fab_cnpj')
fab_inscricaoSC=$(pop 'fab_inscricaoSC')
fab_razaoSocial=$(pop 'fab_razaoSocial')
fab_nomeFantasia=$(pop 'fab_nomeFantasia')
fab_telefone=$(pop 'fab_telefone')
fab_email=$(pop 'fab_email')
fab_endereco=$(pop 'fab_endereco')
fab_logradouro=$(pop 'fab_logradouro')
fab_complemento=$(pop 'fab_complemento')
fab_cep=$(pop 'fab_CEP')
fab_numero=$(pop 'fab_numero')
fab_bairro=$(pop 'fab_bairro')
fab_cidade=$(pop 'fab_cidade')

modelo_daf_nome=$(pop 'modelo_daf_nome')
modelo_daf_chave_ateste_publica=$(pop 'modelo_daf_chave_ateste_publica')

sb_versao=$(pop 'sb_versao')
hsb_resumoash=$(pop 'sb_resumo')
sb_url=$(pop 'sb_url')


#Base WS

linhas="USE \`daf-ws\`;\n"

SQL="START TRANSACTION;\n"
linhas="$linhas$SQL"

if [ ! -z $fab_paf_csrt_hash ] && [ ! -z $cont_cnpj ]; then
    cont_idpaf=`echo -n "$cont_cnpj" | openssl sha256 -binary -hmac "$fab_paf_csrt_hash" | base64 | sed 's/+/-/g; s/\//_/g; s/=//g;'`
fi

#contribuinte
if [ ! -z $cont_cnpj ]; then
    SQL="INSERT INTO pessoa_juridica (cnpj, email, inscricao_estadual_sc, nome_fantasia, razao_social, telefone_principal) VALUES ('$cont_cnpj', '$cont_email', '$cont_inscricaoSC', '$cont_nomeFantasia', '$cont_razaoSocial', '$cont_telefone') ON DUPLICATE KEY UPDATE nome_fantasia = '$fab_paf_razaoSocial', telefone_principal = '$fab_paf_telefone', email = '$fab_paf_email';\n
    SELECT codigo_ibge INTO @cont_cidade FROM municipio WHERE nome = '$cont_cidade' LIMIT 1;\n
    INSERT INTO endereco (bairro, cep, complemento, endereco, logradouro, numero, pessoa_juridica_fk_cnpj, municipio_fk_codigo_ibge) VALUES ('$cont_bairro', '$cont_cep', '$cont_complemento', '$cont_endereco', '$cont_logradouro', '$cont_numero', '$cont_cnpj', @cont_cidade);\n
    INSERT INTO contribuinte (credenciado_nfe, situacao, pessoa_juridica_fk_cnpj) VALUES ($cont_credenciadoNfe, 1, '$cont_cnpj')  ON DUPLICATE KEY UPDATE credenciado_nfe = $cont_credenciadoNfe, SITUACAO = 1;\n"
    linhas="$linhas$SQL"
fi

#fabricante paf
if [ ! -z $fab_paf_cnpj ]; then
    #Fabricante
    SQL="INSERT INTO pessoa_juridica (cnpj, email, inscricao_estadual_sc, nome_fantasia, razao_social, telefone_principal) VALUES ('$fab_paf_cnpj', '$fab_paf_email', '$fab_paf_inscricaoSC', '$fab_paf_nomeFantasia', '$fab_paf_razaoSocial', '$fab_paf_telefone');\n
    SELECT codigo_ibge INTO @fab_paf_cidade FROM municipio WHERE nome = '$fab_paf_cidade' LIMIT 1;\n
    INSERT INTO endereco (bairro, cep, complemento, endereco, logradouro, numero, pessoa_juridica_fk_cnpj, municipio_fk_codigo_ibge) VALUES ('$fab_paf_bairro', '$fab_paf_cep', '$fab_paf_complemento', '$fab_paf_endereco', '$fab_paf_logradouro', '$fab_paf_numero', '$fab_paf_cnpj', @fab_paf_cidade);\n
    INSERT INTO fabricante (daf, paf, pessoa_juridica_fk_cnpj) VALUES (b'0', b'1', '$fab_paf_cnpj');\n
    INSERT INTO csrt (id_csrt, csrt, revogado, fabricante_fk_cnpj) VALUES ($fab_paf_csrt_id, '$fab_paf_csrt_hash', 0, '$fab_paf_cnpj');\n"
    linhas="$linhas$SQL"
fi

#versao paf
if [ ! -z $nome_versao_paf ]; then
    SQL="SELECT pessoa_juridica_fk_cnpj INTO @certificadora FROM certificadora LIMIT 1;\n
    INSERT INTO processo_certificacao (tipo, certificadora_fk_cnpj, fabricante_fk_cnpj) VALUES (1, @certificadora, '$fab_paf_cnpj');\n
    SELECT LAST_INSERT_ID() INTO @procpaf;\n
    INSERT INTO log_processo (comentario, etapa_fk_id, processo_fk_certificacao_id) VALUES ('início', 1, @procpaf), ('fim', 5, @procpaf);\n
    INSERT INTO certificacao (inicio_vigencia, processo_certificacao_fk_id) VALUES (DATE_add(now(), INTERVAL -1 DAY), @procpaf);\n
    SELECT LAST_INSERT_ID() INTO @certificacao;\n
    INSERT INTO versao_paf (nome_versao, certificacao_fk_id, csrt_fk_cnpj, csrt_fk_id_csrt) VALUES ('$nome_versao_paf', @certificacao, '$fab_paf_cnpj', $fab_paf_csrt_id);\n
    INSERT INTO paf_contribuinte (id_paf, ativo, contribuinte_fk_cnpj, versao_paf_fk_nome_versao) VALUES ('$cont_idpaf', 1, '$cont_cnpj', '$nome_versao_paf');\n"
    linhas="$linhas$SQL"
fi

#Modelo Daf
if [ ! -z $modelo_daf_nome ] && [ ! -z $fab_cnpj ] && [ ! -z $sb_versao ]; then
    #Fabricante
    SQL="INSERT INTO pessoa_juridica (cnpj, email, inscricao_estadual_sc, nome_fantasia, razao_social, telefone_principal) VALUES ('$fab_cnpj', '$fab_email', '$fab_inscricaoSC', '$fab_nomeFantasia', '$fab_razaoSocial', '$fab_telefone');\n
    SELECT codigo_ibge INTO @fab_cidade FROM municipio WHERE nome = '$fab_cidade' LIMIT 1;\n
    INSERT INTO endereco (bairro, cep, complemento, endereco, logradouro, numero, pessoa_juridica_fk_cnpj, municipio_fk_codigo_ibge) VALUES ('$fab_bairro', '$fab_cep', '$fab_complemento', '$fab_endereco', '$fab_logradouro', '$fab_numero', '$fab_cnpj', @fab_cidade);\n
    INSERT INTO fabricante (daf, paf, pessoa_juridica_fk_cnpj) VALUES (b'1', b'0', '$fab_cnpj');\n
    SELECT pessoa_juridica_fk_cnpj INTO @certificadora FROM certificadora LIMIT 1;\n
    INSERT INTO processo_certificacao (tipo, certificadora_fk_cnpj, fabricante_fk_cnpj) VALUES (2, @certificadora, '$fab_cnpj');\n
    SELECT LAST_INSERT_ID() INTO @procmodelo;\n
    INSERT INTO log_processo (comentario, etapa_fk_id, processo_fk_certificacao_id) VALUES ('início', 6, @procmodelo), ('fim', 12, @procmodelo);\n
    INSERT INTO certificacao (inicio_vigencia, processo_certificacao_fk_id) VALUES (DATE_add(now(), INTERVAL -1 DAY), @procmodelo);\n
    SELECT LAST_INSERT_ID() INTO @certificacao;\n
    SELECT id INTO @certificado_sef FROM certificado_sef WHERE keystore_file = '$certificado_sef';\n
    SELECT algoritmo_fk_id INTO @algoritmo_id FROM certificado_sef_algoritmo WHERE certificado_sef_fk_id = @certificado_sef LIMIT 1;\n
    INSERT INTO modelo_daf (chave_ateste, nome, certificacao_fk_id, fabricante_fk_cnpj, algoritmo_fk_id) VALUES ('$modelo_daf_chave_ateste_publica', '$modelo_daf_nome', @certificacao, '$fab_cnpj', @algoritmo_id);\n
    SELECT LAST_INSERT_ID() INTO @modeloid;\n    
    INSERT INTO modelo_daf_certificados_sef VALUES ('1',NULL,NULL,DATE_add(now(), INTERVAL -1 DAY),@certificado_sef,@modeloid);\n"
    linhas="$linhas$SQL"

    #software básico
    SQL="INSERT INTO processo_certificacao (tipo, certificadora_fk_cnpj, fabricante_fk_cnpj) VALUES (3, @certificadora, '$fab_cnpj');\n
    SELECT LAST_INSERT_ID() INTO @procsb;\n
    INSERT INTO log_processo (comentario, etapa_fk_id, processo_fk_certificacao_id) VALUES ('início', 13, @procsb), ('fim', 17, @procsb);\n
    INSERT INTO certificacao (inicio_vigencia, processo_certificacao_fk_id) VALUES (DATE_add(now(), INTERVAL -1 DAY), @procsb);\n
    SELECT LAST_INSERT_ID() INTO @certificacao;\n
    INSERT INTO software_basico (data_lancamento, resumo_criptografico, url, versao, certificacao_fk_id) VALUES (DATE_add(now(), INTERVAL -1 HOUR), '$sb_resumo', '$sb_url', $sb_versao, @certificacao);\n
    SELECT LAST_INSERT_ID() INTO @software_basico;\n
    INSERT INTO modelo_daf_software_basico VALUES (@software_basico,@modeloid);\n"
    linhas="$linhas$SQL"
else
    echo "WARNING: Para cadastrar modelo DAF é necessário informa o Fabricante e Versão do Software Básico."        
fi

SQL="COMMIT;\n"
linhas="$linhas$SQL"

#Base PAF
SQL="\nUSE \`daf-paf\`;\n
START TRANSACTION;\n"
linhas="$linhas$SQL"

#contribuinte
if [ ! -z $cont_cnpj ]; then
    SQL="UPDATE pessoa SET nome = '$cont_razaoSocial', telefone_principal = '$cont_telefone', email = '$cont_email' WHERE id = 1;\n
    SELECT codigo_ibge INTO @cont_cidade FROM municipio WHERE nome = '$cont_cidade' LIMIT 1;\n
    INSERT INTO endereco (bairro, cep, complemento, endereco, logradouro, numero, pessoa_fk_id, municipio_fk_codigo_ibge) VALUES ('$cont_bairro', '$cont_cep', '$cont_complemento', '$cont_endereco', '$cont_logradouro', '$cont_numero', 1, @cont_cidade);\n
    UPDATE pessoa_juridica SET cnpj = '$cont_cnpj', nome_fantasia = '$cont_nomeFantasia', inscricao_estadual_sc = '$cont_inscricaoSC' WHERE pessoa_fk_id = 1;\n
    UPDATE empresa SET csc_id = $cont_csc_id, csc = '$cont_csc_hash', ambiente = 2, id_paf = '$cont_idpaf', endereco_sefaz = 'local', tp_emis = 1, nome_certificado = '$cont_ecnpj_nome', senha_certificado = '$cont_ecnpj_senha' WHERE pessoa_juridica_fk_id = 1;\n"
    linhas="$linhas$SQL"
fi

#fabricante paf
if [ ! -z $fab_paf_cnpj ]; then
    #Fabricante
    SQL="UPDATE pessoa SET nome = '$fab_paf_razaoSocial', telefone_principal = '$fab_paf_telefone', email = '$fab_paf_email' WHERE id = 2;\n
    SELECT codigo_ibge INTO @fab_paf_cidade FROM municipio WHERE nome = '$fab_paf_cidade' LIMIT 1;\n
    INSERT INTO endereco (bairro, cep, complemento, endereco, logradouro, numero, pessoa_fk_id, municipio_fk_codigo_ibge) VALUES ('$fab_paf_bairro', '$fab_paf_cep', '$fab_paf_complemento', '$fab_paf_endereco', '$fab_paf_logradouro', '$fab_paf_numero', 2, @fab_paf_cidade);\n
    UPDATE pessoa_juridica SET cnpj = '$fab_paf_cnpj', nome_fantasia = '$fab_paf_nomeFantasia', inscricao_estadual_sc = '$fab_paf_inscricaoSC' WHERE pessoa_fk_id = 2;\n
    UPDATE fornecedor_sistema SET id_csrt = $fab_paf_csrt_id WHERE pessoa_juridica_fk_id = 2;\n"
    linhas="$linhas$SQL"
fi

SQL="COMMIT;\n"
linhas="$linhas$SQL"

echo -e $linhas > $saida



