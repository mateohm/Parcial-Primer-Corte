def afd_a_b_c(cadena: str) -> bool:
    # Estados: q0=0, q1=1, q2=2, q3=3, qdead=-1
    estado = 0  

    for simbolo in cadena:
        if estado == 0:  # q0
            if simbolo == 'a':
                estado = 1
            elif simbolo == 'b':
                estado = 2
            elif simbolo == 'c':
                estado = 3
            else:
                estado = -1

        elif estado == 1:  # q1 (a*)
            if simbolo == 'a':
                estado = 1
            elif simbolo == 'b':
                estado = 2
            elif simbolo == 'c':
                estado = 3
            else:
                estado = -1

        elif estado == 2:  # q2 (b*)
            if simbolo == 'b':
                estado = 2
            elif simbolo == 'c':
                estado = 3
            else:  # 'a'
                estado = -1

        elif estado == 3:  # q3 (c*)
            if simbolo == 'c':
                estado = 3
            else:  # 'a' o 'b'
                estado = -1

        elif estado == -1:  # qdead
            break

    # Estados de aceptación: q0, q1, q2, q3
    return estado in {0, 1, 2, 3}


#  Pruebas
cadenas = ["", "aaa", "bbb", "ccc", "aaabbbccc", "aabb", "bbc", "aba", "cab", "acb"]
for cad in cadenas:
    print(f"{cad!r}: {'ACEPTADA' if afd_a_b_c(cad) else 'RECHAZADA'}")
