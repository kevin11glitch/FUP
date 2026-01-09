# Peça ao usuário para digitar seus dados pessoais (Nome, Endereço, Data de Nascimento, Cidade, CEP, email), verifique se as informações de Data de Nascimento, CEP e email fazem sentido, e mostre ao usuário as informações, se estão todas corretas, ou mostre que alguma informação estava errada.
def verificar_data(data):
    dia = ""
    mes = ""
    ano = ""

    estagio = 0

    for i in data:
        if ord(i) == 47:
            estagio += 1
        else:
            if ord(i) < 48 or ord(i) > 57:
                return "Data errada"
            if estagio == 0:
                dia += i
            elif estagio == 1:
                mes += i
            elif estagio == 2:
                ano += i

    if len(dia) != 2:
        return "Data errada"
    if len(mes) != 2:
        return "Data errada"
    if len(ano) != 4:
        return "Data errada"
    return True

def verificar_cep(cep):
    primeiro = ""
    segundo = ""
    terceiro = ""
    estagio = 0

    for i in cep:
        if ord(i) == 46 or ord(i) == 45:
            estagio += 1
        else:
            if ord(i) < 48 or ord(i) > 57:
                return "CEP errado" 
            
            if estagio == 0:
                primeiro += i
            if estagio == 1:
                segundo += i
            if estagio == 2:
                terceiro += i
    
    if (len(primeiro) != 2) or (len(segundo) != 3) or (len(terceiro) != 3):
        return "CEP errado"
 
    return True

def verificar_email(email):
    cont_arroba = 0
    
    for i in email:
        if i == "@":
            cont_arroba += 1

    if cont_arroba != 1:
        return "E-mail errado"
    
    cont_ponto = 0
    for i in email:
        if i == "." :
            cont_ponto += 1
    if cont_ponto < 1:
        return "E-mail errado"
    
    ponto_colado = False

    for i in range(len(email) - 1):
        if email[i] == "@" and email[i+1] == ".":
            ponto_colado = True
    if ponto_colado:
        return "E-mail errado"
    
    posicao_arroba = 0
    posicao_ultimo_ponto = 0

    for i in range(len(email)):
        if email[i] == "@":
            posicao_arroba = i
        if email[i] == ".":
            posicao_ultimo_ponto = i

    if posicao_ultimo_ponto <= posicao_arroba + 1:
        return "E-mail errado"
    return True



info = {}
info['nome'] = input()
info['endereco'] = input()
info['nascimento'] = input()
info['cidade'] = input()
info['cep'] = input()
info['email'] = input()


email_certo = verificar_email(info['email'])
data_certa = verificar_data(info['nascimento'])
cep_certo = verificar_cep(info['cep'])

if (email_certo == True) and (data_certa == True) and (cep_certo == True):
    print(info)
else:
    if email_certo != True:
        print(email_certo)
    if data_certa != True:
        print(data_certa)
    if cep_certo != True:
        print(cep_certo)