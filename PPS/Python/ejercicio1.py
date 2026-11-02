# Crea un programa Python que comprobe a fortaleza de contrasinais.
# Como mínimo debe comprobar que contén:
# mínimo 8 caracteres.
# maiúsculas e minúsculas
# números
# caracteres especiais
# Debe mostrar un resumo das comprobacións que non se cumpran.


def comprobacion(contraseña):

    tamaño = len(list(contraseña))
    if tamaño < 8:
        print("NO cumple longitud de mas de 8 caracteres")

    elif tamaño >= 8:
        print("cumple longitud de mas de 8 caracteres")

        mayus = 0
        minus = 0

        for x in list(contraseña):
            if x.isupper():
                mayus += 1

            if x.islower():
                minus += 1

        if mayus == 0 or minus == 0:
            return "NO cumple mayusculas y minusculas"
        else:
            print("cumple mayusculas y minusculas")
            numero = 0
            caracter_especial = 0

            for x in list(contraseña):
                if x.isdigit():
                    numero += 1

                if not x.isalnum() and not x.isspace():
                    caracter_especial += 1

            if numero >= 1:
                print("contiene numeros")

                if caracter_especial >= 1:
                    print("tiene caracter especiales")

                elif caracter_especial == 0:
                    print("NO tiene caracteres especiales")

            elif numero == 0:
                print("NO tiene numeros")


password = input("pon una contraseña: ")

comprobacion(password)
