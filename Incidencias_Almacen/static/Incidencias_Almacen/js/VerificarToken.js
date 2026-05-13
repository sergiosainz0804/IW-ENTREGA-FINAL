const token = localStorage.getItem('obtener_token');

if(!token){
    alert('Tienes que iniciar sesion para poder hacer un registro! ');
    window.location.href = window.location.origin + '/Login/';
}
