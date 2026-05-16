const form = document.getElementById('login');

const usuario = document.getElementById('usuario');
const contra = document.getElementById('contra');

// Reglas validacion

const reglasUsuario = [
    { fn: noVacio, msg: 'El usuario no puede estar vacío.' },
    { fn: function (v) { return longitudMinima(v, 3); }, msg: 'El usuario debe tener al menos 3 caracteres.' },
    { fn: function (v) { return longitudMaxima(v, 50); }, msg: 'El usuario no puede superar los 50 caracteres.' }
];

const reglasContra = [
    { fn: noVacio, msg: 'La contraseña no puede estar vacía.' },
    { fn: function (v) { return longitudMinima(v, 4); }, msg: 'La contraseña debe tener al menos 4 caracteres.' }
];

// Validacion al salir

activarValidacionEnVivo(usuario, reglasUsuario);
activarValidacionEnVivo(contra, reglasContra);

// Submit

form.addEventListener('submit', function (e) {
    e.preventDefault();

    const okUsuario = validarCampo(usuario, reglasUsuario);
    const okContra = validarCampo(contra, reglasContra);

    if (!okUsuario || !okContra) return;

    let username = usuario.value;
    let password = contra.value;


    fetch('http://127.0.0.1:8000/api/token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
        .then(function (response) {
            if (response.ok) {
                return response.json();
            } else {
                alert('Credenciales Incorrectas!');
                throw new Error('Credenciales')
            }
        })
        .then(function (data) {
            window.location.href = window.location.origin + '/Menu/';
        });
});