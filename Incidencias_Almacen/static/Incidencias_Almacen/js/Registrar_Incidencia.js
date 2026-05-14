function GuardarIncidencia(){

    const token = TOKEN_GLOBAL; 

   
    fetch('http://127.0.0.1:8000/Incidencias_API/',{
        method: 'POST',
        headers: {
            'Authorization': 'Bearer ' + token, 
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
        })
    })
    .then(function(response){
        if(response.status == 401){
            alert('Tu sesión ha expirado, vuelve a logearte!'); 
     
            window.location.href = window.location.origin + '/Login/';
        }
        return response.json();
    });
}