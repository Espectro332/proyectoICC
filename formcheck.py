def validar(caso):

    errores = []

    if (
        caso["edad"] == "menor"
        and caso["consentimiento"] != "no"
    ):
        errores.append(
            "Si la edad es menor, el consentimiento debe ser 'no'."
        )

    if (
        caso["tipo_usuario"] == "empresa"
        and caso["metodo_pago"] == "efectivo"
    ):
        errores.append(
            "Las empresas no pueden pagar en efectivo."
        )

    if (
        caso["pais"] == "Espana"
        and caso["metodo_pago"] == "efectivo"
    ):
        errores.append(
            "En Espana no se permite el pago en efectivo."
        )

    if (
        caso["tipo_usuario"] == "invitado"
        and caso["metodo_pago"] == "transferencia"
    ):
        errores.append(
            "Los invitados no pueden usar transferencia."
        )

    if (
        caso["edad"] == "adulto"
        and caso["consentimiento"] != "si"
    ):
        errores.append(
            "Si la edad es adulto, el consentimiento debe ser 'si'."
        )

    if (
        caso["pais"] == "Mexico"
        and caso["tipo_usuario"] == "empresa"
        and caso["metodo_pago"] != "transferencia"
    ):
        errores.append(
            "Las empresas de Mexico deben usar transferencia."
        )

    return errores


def backtracking(campos, actual, casos):

    if len(actual) == len(campos):

        caso = {
            "edad": actual[0],
            "pais": actual[1],
            "tipo_usuario": actual[2],
            "metodo_pago": actual[3],
            "consentimiento": actual[4]
        }

        errores = validar(caso)

        if len(errores) == 0:
            caso["estado"] = "Valido"
        else:
            caso["estado"] = "Invalido"

        caso["errores"] = errores

        casos.append(caso)

        return

    indice = len(actual)

    for valor in campos[indice]:

        actual.append(valor)

        backtracking(
            campos,
            actual,
            casos
        )

        actual.pop()


def generar_casos():

    campos = [

        ["menor", "adulto"],

        [
            "Colombia",
            "Mexico",
            "Espana"
        ],

        [
            "estudiante",
            "empresa",
            "invitado"
        ],

        [
            "efectivo",
            "tarjeta",
            "transferencia"
        ],

        [
            "si",
            "no"
        ]
    ]

    casos = []

    backtracking(
        campos,
        [],
        casos
    )

    total = len(casos)

    validos = 0

    for caso in casos:

        if caso["estado"] == "Valido":
            validos += 1

    invalidos = total - validos

    return {
        "total": total,
        "validos": validos,
        "invalidos": invalidos,
        "casos": casos
    }