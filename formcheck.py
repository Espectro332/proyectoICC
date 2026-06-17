def validar(caso):

    errores = []

    if caso["edad"] < 18 and caso["pago"] == "Tarjeta":
        errores.append(
            "Los menores de edad no pueden pagar con tarjeta."
        )

    if caso["consentimiento"] == "No":
        errores.append(
            "El consentimiento es obligatorio."
        )

    if caso["usuario"] == "Premium" and caso["pais"] == "España":
        errores.append(
            "Usuarios Premium no disponibles en España."
        )

    return errores


def backtracking(campos, actual, casos):

    if len(actual) == len(campos):

        caso = {
            "edad": actual[0],
            "pais": actual[1],
            "usuario": actual[2],
            "pago": actual[3],
            "consentimiento": actual[4]
        }

        errores = validar(caso)

        caso["estado"] = (
            "Válido"
            if len(errores) == 0
            else "Inválido"
        )

        caso["errores"] = errores

        casos.append(caso)
        return

    indice = len(actual)

    for valor in campos[indice]:
        actual.append(valor)
        backtracking(campos, actual, casos)
        actual.pop()


def generar_casos():

    campos = [
        [15, 20],
        ["Colombia", "México", "España"],
        ["Básico", "Premium"],
        ["Tarjeta", "Transferencia"],
        ["Sí", "No"]
    ]

    casos = []

    backtracking(campos, [], casos)

    total = len(casos)

    validos = len([
        c for c in casos
        if c["estado"] == "Válido"
    ])

    invalidos = total - validos

    return {
        "total": total,
        "validos": validos,
        "invalidos": invalidos,
        "casos": casos
    }