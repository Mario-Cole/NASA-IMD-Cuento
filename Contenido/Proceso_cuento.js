const btnStart = document.getElementById('btnStart');

btnStart.addEventListener('click', function(e) {
    e.preventDefault(); // Detiene el salto inmediato de página para dejar que ocurra la animación
    const destino = this.getAttribute('href');

    // Activa la clase en el body para disparar las transiciones CSS
    document.body.classList.add('saliendo');

    // Espera 850ms a que la Tierra se aleje y luego cambia a la siguiente página
    setTimeout(() => {
        window.location.href = destino;
    }, 1900);
});