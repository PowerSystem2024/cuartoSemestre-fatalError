function soyAsincrona(mensaje,micallback){
    setTimeout(function() {
        console.log('hola' + mensaje)
        micallback('mensaje de callback')
    }, 1000)
}


function adios(mensaje, otrocallback){
    setTimeout(function() {
        console.log('adios' + mensaje)
        otrocallback('mensaje de otrocallback')
    }, 1000)
}

console.log('inicio')
soyAsincrona('mensaje de prueba',function(mensaje){
    console.log(mensaje)
})
console.log('fin')


