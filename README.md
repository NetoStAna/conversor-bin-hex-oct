# Conversor de Números (Decimais, Binários, Octais e Hexadecimais)

 Repositório contendo um conversor de números decimais, binários, octais e hexadecimais desenvolvido em Python.



## Tipo de Conversão

O algoritmo utiliza uma classe denominada `Conversor` e permite a conversão de números decimais em binários, octais ou hexagonais, assim como a conversão destes em decimais.

```python
def main():
    print("Algoritmo conversor de números!")

    conversor = Conversor()

    print("Digite 1 para realizar uma conversão de decimal para binário!")
    print("Digite 2 para realizar uma conversão de binário para decimal!")
    print("Digite 3 para realizar uma conversão de decimal para octal!")
    print("Digite 4 para realizar uma conversão de octal para decimal!")
    print("Digite 5 para realizar uma conversão de decimal para hexadecimal!")
    print("Digite 6 para realizar uma conversão de hexadecimal para decimal!")
```



## Conversor

A classe `Conversor` possui quatro método de conversão, visto que o processo para números binários e octais é idêntico mudando apenas a base usada para a conversão.



### Decimal Para Base

O método realiza a conversão de números decimais em binários ou octais. Este recebe o número a ser convertido e a base como parâmetro e utiliza uma variável `str`: resultado, inicializada em `""`, assim como um loop `while` que segue enquanto o valor da variável `numero` for diferente de `0`.

```python
    def dec_para_base(self, numero: int, base: int) -> int:
        """ Dado um número decimal converte-o em uma base definida. """

        resultado = ""

        while numero != 0:
```

A cada etapa do loop, a variável `resultado` é atualizada adicionando o resto da divisão da variável `numero` pela variável `base` à `string`. Em seguida, a variável `numero` é atualizada com o valor inteiro da divisão pelo valor da variável `base`.

```python
            resultado += str(numero % base)
            numero //= base
```

Por fim, o inverso da variável `resultado` é retornado, encerrando o método.

```python

        return int(resultado[::-1])
```



### Base Para Decimal

O método realiza a conversão de números binários ou octais em decimais. Este recebe o número a ser convertido e a base como parâmetro e utiliza duas variáveis `int`: exp e resultado, inicializadas em `0`, assim como um loop `while` que segue enquanto o valor da variável `numero` for diferente de `0`.

```python
    def base_para_dec(self, numero: int, base: int) -> int:
        """ Dado um número em uma base definida converte-o em decimal. """

        exp = 0
        resultado = 0

        while numero != 0:
```

A cada etapa do loop, é utilizada uma variável `int`: dec, que obtém o resultado do último algarismo da variável `numero` multiplicado pelo valor da variável `base` elevado ao valor da variável `exp`. Em seguida, a variável `resultado` é atualizada, acrescentando o valor da variável `dec`, o último algarismo da variável `numero` é descartado e a variável `exp` é incrementada em uma unidade.

```python
            dec = (numero % 10) * (base ** exp)
            resultado += dec
            numero //= 10
            exp += 1
```

Por fim, o valor da variável `resultado` é retornado, encerrando o método.

```python

        return resultado
```



### Decimal Para HexaDecimal

O método realiza a conversão de números decimais em hexadecimais. Este recebe o número a ser convertido como parâmetro e utiliza uma variável `str`: resultado, inicializada em `""`, assim como um loop `while` que segue enquanto o valor da variável `numero` for diferente de `0`.

```python
    def dec_para_hex(self, numero: int) -> str:
        """ Dado um número decimal converte-o em hexadecimal. """

        resultado = ""

        while numero != 0:
```

A cada etapa do loop é utilizada uma variável `int`: hex que recebe o resto da divisão entre o valor da variável `numero` por `16`. Em seguida, a variável `hex` é comparada com o valor `10` e, se a primeira for maior ou igual ao segundo, a variável `resultado` é atualizada acrescentando o caractere correspondente ao código `ascii` do valor de `hex` mais `55`.

```python
            hex = numero % 16

            if hex >= 10:
                resultado += chr(hex + 55)
```

Caso contrário, a variável `resultado` é atualizada acrescentando o algarismo da variável `hex`. Em seguida, a variável `numero` é atualizada com o valor inteiro da divisão por `16`.

```python
			else:
        		resultado += str(hex)
            
            numero //= 16
```

Por fim, o inverso da variável `resultado` é retornado, encerrando o método.

```python

        return resultado[::-1]
```



### HexaDecimal para Decimal

O método realiza a conversão de números hexadecimais em decimais. Este recebe o número a ser convertido como parâmetro, utiliza duas variáveis `int`: exp e resultado, inicializadas em `0` e atualiza o valor da variável `numero`, tornando todos os caracteres maiúsculos e invertendo a `string`, assim como um laço `for` que percorre todos os caracteres da variável `numero`.

```python
    def hex_para_dec(self, numero: str) -> int:
        """ Dado um número hexadecimal converte-o em decimal. """

        exp = 0
        resultado = 0
        numero = numero.upper()[::-1]

        for caractere in numero:
```

A cada etapa do laço é verificado se o caractere correspondente é uma letra ou um dígito, caso este seja uma letra é utilizada uma variável `int`: dec, que recebe o valor `ascii` da letra correspondente menos `55` multiplicado por `16` elevado ao valor da variável `exp`.

```python
            if caractere in string.ascii_letters:
                dec = (ord(caractere) - 55) * (16 ** exp)
```

Caso contrário, a variável `dec` recebe o valor correspondente ao dígito do caractere multiplicado por `16` elevado ao valor da variável `exp`. Em seguida, a variável `resultado` é atualizada acrescentando o valor da variável `dec` e a variável `exp` é incrementada em uma unidade.

```python
            else:
                dec = int(caractere) * (16 ** exp)

            resultado += dec
            exp += 1
```

Por fim, a variável `resultado` é retornada, encerrando o método.

```python

        return resultado
```

