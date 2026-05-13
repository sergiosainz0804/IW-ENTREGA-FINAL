

function GuardarIncidencia(){
    const token = localStorage.getItem('obtener_token');

    fetch('http://127.0.0.1:8000/Incidencias_API/',{
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'

        },
        body: JSON.stringify({
        })
        .then(function(response){
            if(response.status == 401){
                alert('Tu sesion ha expirado, vuelve a iniciar sesión!');    
                window.location.href = window.location.origin + '/Login/';
        }
            return response.json()
        })
       
    });
}