fila.innerHTML = `
    <td>${caso.edad}</td>
    <td>${caso.pais}</td>
    <td>${caso.tipo_usuario}</td>
    <td>${caso.metodo_pago}</td>
    <td>${caso.consentimiento}</td>

    <td class="${
        caso.estado === "Valido"
        ? "valido"
        : "invalido"
    }">

        ${caso.estado}

    </td>
`;