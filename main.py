from conversor import Conversor


def main():
    print("Algoritmo conversor de números!")

    conversor = Conversor()

    print("Digite 1 para realizar uma conversão de decimal para binário!")
    print("Digite 2 para realizar uma conversão de binário para decimal!")
    print("Digite 3 para realizar uma conversão de decimal para octal!")
    print("Digite 4 para realizar uma conversão de octal para decimal!")
    print("Digite 5 para realizar uma conversão de decimal para hexadecimal!")
    print("Digite 6 para realizar uma conversão de hexadecimal para decimal!")
    conversao = int(input())

    numero = input("Digite o número a ser convertido: ")

    if conversao != 6:
        numero = int(numero)

    match conversao:
        case 1:
            resultado = conversor.dec_para_base(numero, 2)

        case 2:
            resultado = conversor.base_para_dec(numero, 2)

        case 3:
            resultado = conversor.dec_para_base(numero, 8)

        case 4:
            resultado = conversor.base_para_dec(numero, 8)

        case 5:
            resultado = conversor.dec_para_hex(numero)

        case 6:
            resultado = conversor.hex_para_dec(numero)

    print("Número convertido: " + str(resultado))

if __name__ == "__main__":
    main()
