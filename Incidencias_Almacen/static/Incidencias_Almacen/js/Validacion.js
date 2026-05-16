function mostrarError(campo, mensaje) {
    campo.classList.add('campo-error');
    campo.classList.remove('campo-ok');

    let span = campo.parentElement.querySelector('.aviso-error');
    if (!span) {
        span = document.createElement('span');
        span.className = 'aviso-error';
        campo.parentElement.append(span);
    }
    span.textContent = mensaje;
}

function limpiarError(campo) {
    campo.classList.remove('campo-error');
    campo.classList.add('campo-ok');

    const span = campo.parentElement.querySelector('.aviso-error');
    if (span) span.textContent = '';
}

function limpiarTodosLosErrores(formulario) {
    formulario.querySelectorAll('.campo-error').forEach(function (c) {
        limpiarError(c);
    });
}


// Validacion

function noVacio(valor) {
    return valor.trim().length > 0;
}

function longitudMaxima(valor, max) {
    return valor.trim().length <= max;
}

function longitudMinima(valor, min) {
    return valor.trim().length >= min;
}

function soloAlfanumerico(valor) {
    return /^[a-zA-Z0-9\-_]+$/.test(valor.trim());
}

function esEmail(valor) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(valor.trim());
}

function esTelefono(valor) {
    // Acepta formatos de numeros: +34 612 345 678 / 612345678 / 91 234 56 78
    return /^[\+]?[\d\s\-]{7,15}$/.test(valor.trim());
}

function esCIF(valor) {
    // Formato cif español letra + 7 dígitos + dígito
    return /^[A-HJNP-SUVW]{1}[0-9]{7}[0-9A-J]$/i.test(valor.trim());
}

function selectSeleccionado(valor) {
    return valor !== '' && valor !== null && valor !== undefined;
}

function validarCampo(campo, reglas) {
    const valor = campo.value;
    for (let i = 0; i < reglas.length; i++) {
        if (!reglas[i].fn(valor)) {
            mostrarError(campo, reglas[i].msg);
            return false;
        }
    }
    limpiarError(campo);
    return true;
}


// Validacion instantanea

function activarValidacionEnVivo(campo, reglas) {
    campo.addEventListener('blur', function () {
        validarCampo(campo, reglas);
    });
    campo.addEventListener('input', function () {
        // si hay error revalida
        if (campo.classList.contains('campo-error')) {
            validarCampo(campo, reglas);
        }
    });
}
