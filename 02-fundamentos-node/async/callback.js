function soyAsincrona(mensaje,micallback){
    setTimeout(function() {
        console.log('hola' + mensaje)
        micallback('mensaje de callback')
    }, 1000)
}


function adios(mensaje, otrocallback){
    setTimeout(function() {
        console.log('adios' + mensaje)
        otrocallback()
    }, 1000)
}

// funcion recursiva
function conversacion(Nombre, veces, callback){
    if (veces > 0) {
    hablar(function() {
        conversacion(Nombre, --veces, callback);
    });
    } else {
        callback(Nombre, callback);
    }
}


//--proceso principal
console.log('iniciando proceso')
hola('luca',function(Nombre){
  conversacion('luca', 3, function(){
        console.log("Terminamos el proceso")
    }); 
});







