# Palavra secreta
palavra = ['p','r','o','g','r','a','m','a','ç','ã','o']
letras_digitadas = []

print("Jogo da Forca - Adivinhe a palavra!")

while True:
    letra = input('Digite uma letra: ').lower()

    if len(letra) != 1:
        print('Digite apenas uma letra!')
        continue

    if letra in letras_digitadas:
        print('Você já tentou essa letra.')
        continue

    letras_digitadas.append(letra)

    if letra in palavra:
        print("Você acertou a letra!")
    else:
        print("Você errou a letra!")

    # Mostrar progresso da palavra
    palavra_oculta = ''
    for l in palavra:
        if l in letras_digitadas:
            palavra_oculta += l
        else:
            palavra_oculta += '*'
    
    print('Palavra:', palavra_oculta)

    # Verifica se o jogador venceu
    if '*' not in palavra_oculta:
        print("Parabéns! Você acertou a palavra completa!")
        break
# jogo-da-forca-me-python
