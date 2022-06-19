
plataforma = [' ' for x in range(10)]


def inserirLetra(letra, posicao):
    plataforma[posicao] = letra

def espacoVazio(posicao):  # ESPAÇO DA PLATAFORMA ESTÁ VAZIO?
    return plataforma[posicao] == ' '

def desenharPlataforma(plataforma):
    print('   |   |')
    print(' ' + plataforma[1] + ' | ' + plataforma[2] + ' | ' + plataforma[3] )
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + plataforma[4] + ' | ' + plataforma[5] + ' | ' + plataforma[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + plataforma[7] + ' | ' + plataforma[8] + ' | ' + plataforma[9])
    print('   |   |')

def Vencedor(pltfm, ltr):  # PLTFM E LTR ESTÃO ASSOCIADOS A PLATAFORMA E LETRA PARA CHECAR O VENCEDOR
    return (pltfm[7] == ltr and pltfm[8] == ltr and pltfm[9] == ltr) or \  # A SEQUÊNCIA DA POSIÇÃO 7 8 E 9 DA PLATAFORMA ESTÁ COM AS MESMAS LETRAS?
           (pltfm[4] == ltr and pltfm[5] == ltr and pltfm[6] == ltr) or \
           (pltfm[1] == ltr and pltfm[2] == ltr and pltfm[3] == ltr) or \
           (pltfm[1] == ltr and pltfm[4] == ltr and pltfm[7] == ltr) or \
           (pltfm[2] == ltr and pltfm[5] == ltr and pltfm[8] == ltr) or \
           (pltfm[3] == ltr and pltfm[6] == ltr and pltfm[9] == ltr) or \
           (pltfm[1] == ltr and pltfm[5] == ltr and pltfm[9] == ltr) or \
           (pltfm[3] == ltr and pltfm[5] == ltr and pltfm[7] == ltr) or


def movJogador():
    pass

def compMove():
    pass

def selecionaRandom(board):
    pass

def plataformaFull(board):
    pass

def main():
    pass

main()
