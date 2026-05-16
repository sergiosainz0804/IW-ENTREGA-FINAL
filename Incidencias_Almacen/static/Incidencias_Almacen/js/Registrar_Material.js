const form = document.querySelector('form');

const nombre = document.getElementById('id_nombre');
const codigo = document.getElementById('id_codigo_interno');
const descripcion = document.getElementById('id_descripcion');
const familia = document.getElementById('id_familia');
const ubicacion = document.getElementById('id_ubicacion_habitual');

// Reglas

const reglasNombre = [
    { fn: noVacio, msg: 'El nombre es obligatorio.' },
    { fn: function (v) { return longitudMinima(v, 2); }, msg: 'El nombre debe tener al menos 2 caracteres.' },
    { fn: function (v) { return longitudMaxima(v, 150); }, msg: 'Máximo 150 caracteres.' }
];

const reglasCodigo = [
    { fn: noVacio, msg: 'El código interno es obligatorio.' },
    { fn: function (v) { return longitudMaxima(v, 50); }, msg: 'Máximo 50 caracteres.' },
    { fn: soloAlfanumerico, msg: 'Solo letras, números, guiones y guiones bajos.' }
];

const reglasDescripcion = [
    { fn: noVacio, msg: 'La descripción es obligatoria.' },
    { fn: function (v) { return longitudMinima(v, 5); }, msg: 'La descripción debe tener al menos 5 caracteres.' }
];

const reglasFamilia = [
    { fn: noVacio, msg: 'La familia es obligatoria.' },
    { fn: function (v) { return longitudMaxima(v, 100); }, msg: 'Máximo 100 caracteres.' }
];

const reglasUbicacion = [
    { fn: noVacio, msg: 'La ubicación habitual es obligatoria.' },
    { fn: function (v) { return longitudMaxima(v, 100); }, msg: 'Máximo 100 caracteres.' }
];

// Validacion intantanea

if (nombre) activarValidacionEnVivo(nombre, reglasNombre);
if (codigo) activarValidacionEnVivo(codigo, reglasCodigo);
if (descripcion) activarValidacionEnVivo(descripcion, reglasDescripcion);
if (familia) activarValidacionEnVivo(familia, reglasFamilia);
if (ubicacion) activarValidacionEnVivo(ubicacion, reglasUbicacion);

// Submit

form.addEventListener('submit', function (e) {
    e.preventDefault();

    let valido = true;

    if (nombre && !validarCampo(nombre, reglasNombre)) valido = false;
    if (codigo && !validarCampo(codigo, reglasCodigo)) valido = false;
    if (descripcion && !validarCampo(descripcion, reglasDescripcion)) valido = false;
    if (familia && !validarCampo(familia, reglasFamilia)) valido = false;
    if (ubicacion && !validarCampo(ubicacion, reglasUbicacion)) valido = false;

    if (!valido) {
        alert('Revisa los campos marcados en rojo antes de continuar.');
        return;
    }

    form.submit();
});
