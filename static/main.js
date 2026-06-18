const boton = document.getElementById("generar");

const tabla = document.querySelector("#tabla tbody");

const detalle = document.getElementById("detalle");

boton.addEventListener("click", async () => {

    const response = await fetch("/generar");

    const data = await response.json();

    document.getElementById("total").textContent =
        data.total;

    document.getElementById("validos").textContent =
        data.validos;

    document.getElementById("invalidos").textContent =
        data.invalidos;

    tabla.innerHTML = "";

    data.casos.forEach(caso => {

        const fila = document.createElement("tr");

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

        fila.addEventListener("click", () => {

            if (caso.errores.length === 0) {

                detalle.innerHTML = `
                    <h3>Caso válido</h3>
                    <p>Este caso cumple todas las reglas.</p>
                `;

            } else {

                detalle.innerHTML = `
                    <h3>Reglas incumplidas</h3>
                    <ul>
                        ${caso.errores
                            .map(error => `<li>${error}</li>`)
                            .join("")}
                    </ul>
                `;
            }

        });

        tabla.appendChild(fila);

    });

});