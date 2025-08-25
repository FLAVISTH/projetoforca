import desenhos as d
print("Bem vindo ao jogo da forca!")
palavra = input('digite uma palavra secreta: ').lower().strip()

for x in range(50):
    print()

digitadas = []
acertos   = []
erros     = 0

while True:
    adivinha = d.imprimir_palavra_secreta(palavra, acertos)
    
    # * CONDIÇÃO DE VITORIA
    if adivinha == palavra:
        print("você acertou!")
        break

    # * TENTATIVAS
    tentativa = input("\nDigite uma letra:" ).lower().strip()
    if tentativa in digitadas :
        print("você já usou essa letra!")
        continue
    else:
        digitadas += tentativa 
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("você errou!")

    
    d.desenhar_forca(erros)
    
    # * CONDIÇÃO DE FIM DE JJOGO 
    if erros == 6:
        print("ENFORCADO")
        print(f"A palavra correta era {palavra}. ")
        break
    
