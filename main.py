
plataforma = [' ' for x in range(10)]


def inserirletra(letra, posicao):
    plataforma[posicao] = letra


def espacovazio(posicao):  # ESPAÇO DA PLATAFORMA ESTÁ VAZIO?
    return plataforma[posicao] == ' '


def desenharplataforma(plataforma):
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
    return (pltfm[7] == ltr and pltfm[8] == ltr and pltfm[9] == ltr) \
           or (pltfm[4] == ltr and pltfm[5] == ltr and pltfm[6] == ltr) \
           or (pltfm[1] == ltr and pltfm[2] == ltr and pltfm[3] == ltr) \
           or (pltfm[1] == ltr and pltfm[4] == ltr and pltfm[7] == ltr) \
           or (pltfm[2] == ltr and pltfm[5] == ltr and pltfm[8] == ltr) \
           or (pltfm[3] == ltr and pltfm[6] == ltr and pltfm[9] == ltr) \
           or (pltfm[1] == ltr and pltfm[5] == ltr and pltfm[9] == ltr) \
           or (pltfm[3] == ltr and pltfm[5] == ltr and pltfm[7] == ltr)


def movjogador():
    pass


def compomve():
    pass


def selecionarandom(plataforma):
    pass


def plataformafull(plataforma):
    pass


def main():
    pass


main()
