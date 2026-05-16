const form = document.querySelector('form');

const nombreComercial = document.getElementById('id_nombre_comercial');
const email = document.getElementById('id_email');
const telefono = document.getElementById('id_telefono');
const cif = document.getElementById('id_cif');
const direccion = document.getElementById('id_direccion');

// reglas

const reglasNombre = [
    { fn: noVacio, msg: 'El nombre comercial es obligatorio.' },
    { fn: function (v) { return longitudMinima(v, 2); }, msg: 'Debe tener al menos 2 caracteres.' },
    { fn: function (v) { return longitudMaxima(v, 150); }, msg: 'Máximo 150 caracteres.' }
];

const reglasEmail = [
    { fn: noVacio, msg: 'El email es obligatorio.' },
    { fn: esEmail, msg: 'Introduce un email válido (ej: empresa@dominio.com).' }
];

const reglasTelefono = [
    { fn: noVacio, msg: 'El teléfono es obligatorio.' },
    { fn: esTelefono, msg: 'Introduce un teléfono válido (7-15 dígitos, puede incluir +, espacios y guiones).' }
];

const reglasCIF = [
    { fn: noVacio, msg: 'El CIF es obligatorio.' },
    { fn: esCIF, msg: 'Formato de CIF inválido (ej: A1234567H).' }
];

const reglasDireccion = [
    { fn: noVacio, msg: 'La dirección es obligatoria.' },
    { fn: function (v) { return longitudMinima(v, 5); }, msg: 'La dirección debe tener al menos 5 caracteres.' },
    { fn: function (v) { return longitudMaxima(v, 200); }, msg: 'Máximo 200 caracteres.' }
];

// Validacion instantanea

if (nombreComercial) activarValidacionEnVivo(nombreComercial, reglasNombre);
if (email) activarValidacionEnVivo(email, reglasEmail);
if (telefono) activarValidacionEnVivo(telefono, reglasTelefono);
if (cif) activarValidacionEnVivo(cif, reglasCIF);
if (direccion) activarValidacionEnVivo(direccion, reglasDireccion);

// Submit
form.addEventListener('submit', function (e) {
    e.preventDefault();

    let valido = true;

    if (nombreComercial && !validarCampo(nombreComercial, reglasNombre)) valido = false;
    if (email && !validarCampo(email, reglasEmail)) valido = false;
    if (telefono && !validarCampo(telefono, reglasTelefono)) valido = false;
    if (cif && !validarCampo(cif, reglasCIF)) valido = false;
    if (direccion && !validarCampo(direccion, reglasDireccion)) valido = false;

    if (!valido) {
        alert('Revisa los campos marcados en rojo antes de continuar.');
        return;
    }

    form.submit();
});
