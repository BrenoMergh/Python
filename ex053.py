frase = str(input('Digite uma frase: ')).strip().upper()
#strip() tira os espaços antes e depois da frase
#upper() deixa tudo em maiúscula
palavras = frase.split()
#split() tira todos os espaços no meio da frase e separa elas em lista
junto = ''.join(palavras)
#join() junta a string em uma lista e coloca entre elas o que tem entre os '' ex:[o,amor,é,cego] vira [oamorécego]
reverso = junto[::-1]
#aqui pegamos o reverso da frase(junto) pois estamos indo do inicio qualquer pois nao foi colocado qual inicio ate o final qualquer pela mesma razão e estamos indo de tras pra frente(-1)
if junto == reverso:
    print('\033[1;30;42mÉ um palíndromo\033[m')
else:
    print('\033[1;30;41mNão é um palíndromo\033[m')
