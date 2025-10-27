function hola(nombre, micallback)   {
    setTimeout(function() {
        console.log('hola' + nombre)
        micallback('mensaje de callback')
    }, 1000)
}

function hablar (callbackhablar){
    setTimeout(function() {
        console.log('hablando')
        callbackhablar()
    }, 1000)
}

function adios(mensaje, otrocallback){
    setTimeout(function() {
        console.log('adios' + mensaje)
        otrocallback()
    }, 1000)
}