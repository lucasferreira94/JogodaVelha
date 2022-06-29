
plataforma = [' ' for x in range(10)]


def inserir_letra(letra, posicao):
    plataforma[posicao] = letra


def espaco_vazio(posicao):                                    # ESPAÇO DA PLATAFORMA ESTÁ VAZIO?
    return plataforma[posicao] == ' '


def desenha_plataforma(plataforma):
    print('   |   |')
    print(' ' + plataforma[1] + ' | ' + plataforma[2] + ' | ' + plataforma[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + plataforma[4] + ' | ' + plataforma[5] + ' | ' + plataforma[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + plataforma[7] + ' | ' + plataforma[8] + ' | ' + plataforma[9])
    print('   |   |')


# PLTFM E LTR ESTÃO ASSOCIADOS A PLATAFORMA E LETRA PARA CHECAR O VENCEDOR
# A SEQUÊNCIA DA POSIÇÕES {X Y Z} DA PLATAFORMA ESTÃO COM AS MESMAS LETRAS?

def vencedor(pltfm, ltr):
    return (pltfm[1] == ltr and pltfm[2] == ltr and pltfm[3] == ltr) \
           or (pltfm[4] == ltr and pltfm[5] == ltr and pltfm[6] == ltr) \
           or (pltfm[7] == ltr and pltfm[8] == ltr and pltfm[9] == ltr) \
           or (pltfm[1] == ltr and pltfm[4] == ltr and pltfm[7] == ltr) \
           or (pltfm[2] == ltr and pltfm[5] == ltr and pltfm[8] == ltr) \
           or (pltfm[3] == ltr and pltfm[6] == ltr and pltfm[9] == ltr) \
           or (pltfm[1] == ltr and pltfm[5] == ltr and pltfm[9] == ltr) \
           or (pltfm[3] == ltr and pltfm[5] == ltr and pltfm[7] == ltr)


def mov_jogador():
    run = True
    while run:
        mov = input('Por favor, selecione a posição para colocar o \"X\" (1-9): ')
        try:                                                #  TRATAMENTO DE ERRO PARA ACEITAR APENAS:
            mov = int(mov)                                  #  POSIÇÃO PARA MOVIMENTAÇÃO NUMEROS ENTRE {0 E 10}
            if mov > 0 and mov < 10:
                if espaco_vazio(mov):                       #  SE O ESPAÇO DO MOVIMENTO ESTIVER VAZIO, NÃO SERÁ NECESSÁRIO EXIBIR
                    run = False                             # A MENSAGEM AO USUÁRIO (POR FAVOR, SELECIONE A POS...) E A LETRA SERÁ INSERIDA
                    inserir_letra('X', mov)
                else:
                    print('Desculpe, o espaço está ocupado')
            else:
                print('Por favor, digite um número dentro do range (1-9)')
        except:
            print('Por favor, digite um número')


def mov_computador():
    mov_possiveis = [x for x, letra in enumerate(plataforma) if letra == ' ' and x != 0]  # HÁ UM ESPAÇO VAZIO QUE POSSA SER FEITO UM MOVIMENTO?
    mov = 0
                                                            #  LOOP IRÁ CHECAR SE AS POSSIÇÕES DISPONÍVEIS, QUAL O COMP PODE VENCER
    for letra in ['O', 'X']:                                #  O LOOP TAMBÉM CHECA AS POSSIBILIDADES DO JOGADOR HUMANO GANHAR 'X'
        for i in mov_possiveis:                             #  PEGA OS MOVS POSSÍVEIS, IDENTIFICANDO QUALQUER ESPAÇO VAZIO
            copia_plataforma = plataforma[:]
            copia_plataforma[i] = letra                     #  COLOCA A LETRA NA POSIÇÃO VAZIA EM UMA PLATAFORMA COPIADA DA ORIGINAL
            if vencedor(copia_plataforma, letra):           #  COM ESSE MOV, É POSSÍVEL GANHAR? SE SIM, ESSE SERÁ O MOV FINAL
                mov = i
                return mov

    canto_aberto = []
    for i in mov_possiveis:
        if i in [1,3,7,9]:
            canto_aberto.append(i)

    if len(canto_aberto) > 0:                               # CASO TENHA MAIS DE UMA POSICAO DOS CANTOS DISPONÍVEIS (1,3,7,9) SELECIONA QUALQUER UMA DELAS
        mov = seleciona_random(canto_aberto)
        return mov

    if 5 in mov_possiveis:                                  # POSICAO DO CENTRO DISPONÍVEL? FAÇA O MOV NELA
        mov = 5
        return mov

    borda_aberta = []
    for i in mov_possiveis:
        if i in [2,4,6,8]:
            borda_aberta.append(i)

    if len(borda_aberta) > 0:
        mov = seleciona_random(borda_aberta)

    return mov                                              # SE NENHUMA POSSIBILIDADE ANTERIOR FOR POSSÍVEL, MOV SERÁ '0'


def seleciona_random(lista):
    import random
    ln = len(lista)
    r = random.randrange(0,ln)
    return lista[r]


def plataforma_full(plataforma):
    if plataforma.count(' ') > 1:                         # POSSUI MAIS DE 1 ESPAÇO VAZIO? ENTÃO A PLATAFORMA ESTÁ CHEIA
        return False
    else:
        return True


def main():
    print('Bem vindo ao JOGO DA VELHA!', '\n')
    desenha_plataforma(plataforma)

    while not(plataforma_full(plataforma)):             # ENQUANTO A PLATAFORMA NÃO ESTÁ VAZIA, CONTINUA O JOGO
        if not (vencedor(plataforma, 'O')):             # VENCEDOR NÂO É O '0' ?
            mov_jogador()                               # JOGADOR 1 PODERÁ FAZER SEU MOVIMENTO
            desenha_plataforma(plataforma)
        else:
            print('Desculpe, \{O\} ganhou o jogo!')
            break

        if not (vencedor(plataforma, 'X')):             # VENCEDOR NÃO É O 'x'?
            mov = mov_computador()                      # JOGADOR 2 PODERÁ FAZER SEU MOVIMENTO
            if mov == 0:                                # IRÁ CHECAR SE O COMPUTADOR CONSEGUIU FAZER ALGUM MOVIMENTO
                print('EMPATE!')
            else:
                inserir_letra('O', mov)
                print('Computador colocou \"O\" na posição', mov, ':')
                desenha_plataforma(plataforma)
        else:
            print('\{X\} ganhou o jogo dessa vez! ')
            break

    if plataforma_full(plataforma):
        print('EMPATE!')


while True:
    resposta = input('Deseja jogar novamente? [S/N] ')
    if resposta.lower == 's' or resposta.lower == 'sim':
        print('---------------------------------------' '\n')
        main()
    else:
        print('Fim de jogo!')
        exit(0)
