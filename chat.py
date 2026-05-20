nome = ""
idade = 0
altura = 0.0
peso = 0.0
genero = ""
resposta = ""

print("Saudações caro viajante, poderia me dizer seu nome?")
resposta = input().lower()

if 'nome é' in resposta:
    nome = resposta [resposta.find('nome é') + 6:].strip().capitalize()
    print("Seja bem-vindo, " + nome + "!")

elif 'chamo' in resposta:
    nome = resposta [resposta.find('chamo') + 5:].strip().capitalize()
    print("Seja bem-vindo, " + nome + "!")

else:
    print("Você se chama mesmo " + resposta.capitalize() + "?")
    reposta = input().lower()

    if 'sim' in reposta:
        nome = resposta.capitalize()
        print ("Seja bem-vindo, " + nome + "!")

    else:
        print("Poderia me dizer somente o seu nome por favor?")
        nome = input().capitalize()
        print ("Seja bem-vindo, " + nome + "!")