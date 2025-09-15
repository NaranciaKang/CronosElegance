console.log("Js cargando");

const carrito = document.getElementById('carrito');
const elemento1 = document.getElementById('lista-1');
const lista = document.querySelector('#lista-carrito tbody');
const vaciarCarritoBtn = document.getElementById('vaciar-carrito');

cargarEventListener();

function cargarEventListener () {
    elemento1.addEventListener('click', comprarElemento);
    carrito.addEventListener('click', eliminarElemento);
    vaciarCarritoBtn.addEventListener('click', vaciarCarrito);
}

function comprarElemento(e) {
    e.preventDefault();
    if(e.target.classList.contains('agregar-carrito')) {
        const elemento = e.target.parentElement.parentElement;
        leerDatosElemento(elemento);
        mostrarNotificacion("Producto añadido correctamente al carrito");
    }
}

function mostrarNotificacion(mensaje) {
    const notificacion = document.getElementById("notificacion")
    notificacion.textContent = mensaje;
    notificacion.classList.add("mostrar")

    setTimeout(() => {
        notificacion.classList.remove("mostrar")
    }, 2000)
}

function leerDatosElemento(elemento) {
    const infoElemento = {
        imagen: elemento.querySelector('img').src,
        titulo: elemento.querySelector('h3').textContent,
        precio: elemento.querySelector('.precio').textContent,
        id: elemento.querySelector('a').getAttribute('data-id')
    }
    insertarCarrito(infoElemento);
}

function insertarCarrito(elemento) {
    const row = document.createElement('tr');
    row.innerHTML = `
        <td>
            <img src="${elemento.imagen}" width=100 />
        </td>
        <td>
            ${elemento.titulo}
        </td>
        <td>
            ${elemento.precio}
        </td>
        <td>
            <a href="#" class="borrar" data-id="${elemento.id}">X </a>
        </td>
    `;
    lista.appendChild(row);
}

function eliminarElemento(e) {
    e.preventDefault();
    let elemento,
        elementoId;
    if(e.target.classList.contains('borrar')) {
        e.target.parentElement.parentElement.remove();
        elemento = e.target.parentElement.parentElement;
        elementoId = elemento.querySelector('a').getAttribute('data-id');
    }
}



function vaciarCarrito(e) {
    e.preventDefault();
    while(lista.firstChild) {
        lista.removeChild(lista.firstChild);
    }
    return false;
}

document.addEventListener("click", function(e) {
    if(e.target.classList.contains("agregar-wishlist")) {
        e.preventDefault();
        const productoId = e.target.getAttribute("data-id");

        fetch(`/wishlist/toggle/${productoId}/`, {
            method: "GET",
            headers: {
                "X-Requested-With": "XMLHttpRequest"
            }
        })
        .then(res => res.json())
        .then(data => {
            mostrarNotificacion(data.message);
            if (data.status === "added") {
                e.target.textContent = "💔 Quitar de wishlist";
            } else {
                e.target.textContent = "💖 Wishlist";
            }
        })
        .catch(err => console.error(err));
    }
});
