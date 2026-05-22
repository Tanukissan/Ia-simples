from string import punctuation

nome = ""
resposta = input("Saudações caro viajante, poderia me dizer seu nome? ").lower()


if 'nome é' in resposta:
    nome = resposta [resposta.find('nome é') + 6:].lstrip()            #Coloca o nome do usuário no começo do texto
    nome = "".join([char for char in nome if char not in punctuation]) #Limpa os caracteres especiais da frase
    nome = nome [0 :nome.find(" ") + 1:].strip().capitalize()          #Deixa somente o primeiro nome do usuário na variável
    print("Seja bem-vindo, {}!".format(nome))

#Os blocos a baixo tem a mesma função, mas para outras estruturas de frases

elif 'chamo' in resposta:
    nome = resposta [resposta.find('chamo') + 5:].lstrip()
    nome = "".join([char for char in nome if char not in punctuation])
    nome = nome [0 :nome.find(" ") + 1:].strip().capitalize()
    print("Seja bem-vindo, {}!".format(nome))

else:
    reposta = input("Você se chama mesmo {}?".format(resposta.capitalize())).lower()

    if 'sim' in reposta:
        nome = resposta.capitalize()
        print ("Seja bem-vindo, {}!".format(nome))

    else:
        nome = input("Poderia me dizer somente o seu nome por favor?").capitalize()
        print ("Seja bem-vindo, {}!".format(nome))


#while 'encerrar conversa' not in resposta:
#    resposta = input("O que mais você gostaria de me contar sobre você?").lower()
    
    