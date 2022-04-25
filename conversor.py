""" Conversor de números

Decimais, Binários, Octais e Hexadecimais.
"""

import string


class Conversor:
    def dec_para_base(self, numero: int, base: int) -> int:
        """ Dado um número decimal converte-o em uma base definida. """

        resultado = ""

        while numero != 0:
            resultado += str(numero % base)
            numero //= base

        return int(resultado[::-1])

    def base_para_dec(self, numero: int, base: int) -> int:
        """ Dado um número em uma base definida converte-o em decimal. """

        exp = 0
        resultado = 0

        while numero != 0:
            dec = (numero % 10) * (base ** exp)
            resultado += dec
            numero //= 10
            exp += 1

        return resultado

    def dec_para_hex(self, numero: int) -> str:
        """ Dado um número decimal converte-o em hexadecimal. """

        resultado = ""

        while numero != 0:
            hex = numero % 16

            if hex >= 10:
                resultado += chr(hex + 55)
            else:
                resultado += str(hex)

            numero //= 16

        return resultado[::-1]

    def hex_para_dec(self, numero: str) -> int:
        """ Dado um número hexadecimal converte-o em decimal. """

        exp = 0
        resultado = 0
        numero = numero.upper()[::-1]

        for caractere in numero:
            if caractere in string.ascii_letters:
                dec = (ord(caractere) - 55) * (16 ** exp)
            else:
                dec = int(caractere) * (16 ** exp)

            resultado += dec
            exp += 1

        return resultado
