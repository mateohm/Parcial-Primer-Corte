def afd_identificador(cadena: str) -> bool:
    estado = 0  # q0 inicial

    for i, simbolo in enumerate(cadena):
        if estado == 0:  # q0
            if simbolo.isalpha():  # primera debe ser letra
                estado = 1
            else:
                estado = -1
                break

        elif estado == 1:  # q1 (identificador valido)
            if simbolo.isalnum():  # letra o numero
                estado = 1
            else:
                estado = -1
                break

    return estado == 1


# Pruebas
if __name__ == "__main__":
    pruebas = ["Hola123", "a", "Z9prueba", "123abc", "@test"]
    for cad in pruebas:
        print(f"{cad!r}: {'ACEPTADA' if afd_identificador(cad) else 'RECHAZADA'}")
