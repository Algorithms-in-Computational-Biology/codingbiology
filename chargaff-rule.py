
def pair(argument):
    switcher = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
    }
    return switcher.get(argument, "X")

def complemento(sequence):
    res = ''
    for x in sequence:
        y = pair(x)    
        res = res + y
    return res

def main():
    print('Regra de Chargaff')

    entrada = 'ATCG'

    print('Entrada:' + entrada)

    saida = complemento(entrada)

    print('Entrada:' + saida)

if __name__ == "__main__":
    main()


