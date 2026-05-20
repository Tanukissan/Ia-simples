nome = ""
idade = 0
altura = 0.0
peso = 0.0
genero = ""

resposta = input("Saudações caro viajante, poderia me dizer seu nome?").lower()

if 'nome é' in resposta:
    nome = resposta [resposta.find('nome é') + 6:].strip().capitalize()
    print("Seja bem-vindo, " + nome + "!")

elif 'chamo' in resposta:
    nome = resposta [resposta.find('chamo') + 5:].strip().capitalize()
    print("Seja bem-vindo, " + nome + "!")

else:
    reposta = input("Você se chama mesmo " + resposta.capitalize() + "?").lower()

    if 'sim' in reposta:
        nome = resposta.capitalize()
        print ("Seja bem-vindo, " + nome + "!")

    else:
        nome = input("Poderia me dizer somente o seu nome por favor?").capitalize()
        print ("Seja bem-vindo, " + nome + "!")