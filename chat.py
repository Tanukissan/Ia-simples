from string import punctuation

nome = ""
resposta = ""

def limpa_char(itemA):  #Limpa os caracteres especiais da frase
    itemA = "".join([char for char in itemA if char not in punctuation]) 
    itemA = itemA [0 :itemA.find(" ") + 1:].strip().capitalize()
    return itemA

def chama_nome(frase):
    if 'nome é' in frase:
        nome = frase [frase.find('nome é') + 6:].lstrip()
        nome = limpa_char(nome)
        
    elif 'chamo' in frase:
        nome = frase [frase.find('chamo') + 5:].lstrip()
        nome = limpa_char(nome)

    else:
        frase = input("Você se chama mesmo {}?".format(frase.capitalize())).lower()

        if 'sim' in frase:
            nome = frase.capitalize()
            
        else:
            nome = input("Poderia me dizer somente o seu nome por favor?").capitalize()
    return nome

resposta = input("Poderia me dizer seu nome? ").lower()
nome = chama_nome(resposta)
print("Prazer em te conhecer, {}!".format(nome))

#while 'encerrar conversa' not in resposta:
#    resposta = input("O que mais você gostaria de me contar sobre você?").lower()
    
    