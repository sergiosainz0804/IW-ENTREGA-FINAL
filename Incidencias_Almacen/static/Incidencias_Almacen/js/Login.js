
const form = document.getElementById('login');


form.addEventListener('submit', function(e){
    e.preventDefault()

    const usuario = document.getElementById('usuario');
    const contra = document.getElementById('contra');

    username = usuario.value;
    password = contra.value;



fetch('http://127.0.0.1:8000/api/token/', {
    method : 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({username, password})
})
.then(function(response) {
    if(response.ok){
        return response.json()
    }else{
        throw Error('Credenciales Incorrectas');
    }
})
.then(function(data){
    localStorage.setItem('obtener_token', data.access);
    localStorage.setItem('refresh_token', data.refresh);

    window.location.href = window.location.origin + '/Menu/';
});
});

