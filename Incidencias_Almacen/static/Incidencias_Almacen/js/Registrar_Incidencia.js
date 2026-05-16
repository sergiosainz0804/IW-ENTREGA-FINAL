const form = document.querySelector('form');

const codigo = document.getElementById('id_codigo');
const titulo = document.getElementById('id_titulo');
const descripcion = document.getElementById('id_descripcion_detallada');
const estado = document.getElementById('id_estado');
const prioridad = document.getElementById('id_nivel_prioridad');
const zona = document.getElementById('id_zona_almacen');

// reglas

const reglasCodigo = [
    { fn: noVacio, msg: 'El código es obligatorio.' },
    { fn: function (v) { return longitudMaxima(v, 50); }, msg: 'Máximo 50 caracteres.' },
    { fn: soloAlfanumerico, msg: 'Solo letras, números, guiones y guiones bajos.' }
];

const reglasTitulo = [
    { fn: noVacio, msg: 'El título es obligatorio.' },
    { fn: function (v) { return longitudMinima(v, 5); }, msg: 'El título debe tener al menos 5 caracteres.' },
    { fn: function (v) { return longitudMaxima(v, 200); }, msg: 'Máximo 200 caracteres.' }
];

const reglasDescripcion = [
    { fn: noVacio, msg: 'La descripción es obligatoria.' },
    { fn: function (v) { return longitudMinima(v, 10); }, msg: 'La descripción debe tener al menos 10 caracteres.' }
];

const reglasEstado = [
    { fn: selectSeleccionado, msg: 'Selecciona un estado.' }
];

const reglasPrioridad = [
    { fn: selectSeleccionado, msg: 'Selecciona un nivel de prioridad.' }
];

const reglasZona = [
    { fn: noVacio, msg: 'La zona de almacén es obligatoria.' },
    { fn: function (v) { return longitudMaxima(v, 100); }, msg: 'Máximo 100 caracteres.' }
];

// Validacion instantanea

if (codigo) activarValidacionEnVivo(codigo, reglasCodigo);
if (titulo) activarValidacionEnVivo(titulo, reglasTitulo);
if (descripcion) activarValidacionEnVivo(descripcion, reglasDescripcion);
if (estado) activarValidacionEnVivo(estado, reglasEstado);
if (prioridad) activarValidacionEnVivo(prioridad, reglasPrioridad);
if (zona) activarValidacionEnVivo(zona, reglasZona);

// Submut

form.addEventListener('submit', function (e) {
    e.preventDefault();

    let valido = true;

    if (codigo && !validarCampo(codigo, reglasCodigo)) valido = false;
    if (titulo && !validarCampo(titulo, reglasTitulo)) valido = false;
    if (descripcion && !validarCampo(descripcion, reglasDescripcion)) valido = false;
    if (estado && !validarCampo(estado, reglasEstado)) valido = false;
    if (prioridad && !validarCampo(prioridad, reglasPrioridad)) valido = false;
    if (zona && !validarCampo(zona, reglasZona)) valido = false;

    if (!valido) {
        alert('Revisa los campos marcados en rojo antes de continuar.');
        return;
    }

    form.submit();
});


function GuardarIncidencia() {

    const token = TOKEN_GLOBAL;


    fetch('http://127.0.0.1:8000/Incidencias_API/', {
        method: 'POST',
        headers: {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
        })
    })
        .then(function (response) {
            if (response.status == 401) {
                alert('Tu sesión ha expirado, vuelve a logearte!');

                window.location.href = window.location.origin + '/Login/';
            }
            return response.json();
        });
}