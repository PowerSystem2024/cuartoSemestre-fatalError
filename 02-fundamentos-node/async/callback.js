function soyAsincrona(callback){
    setTimeout(function(micallback) {
        console.log('soy una funcion asincrona')
    }, 1000)
}

console.log('inicio')
soyAsincrona(function(mensaje){
    console.log(mensaje)
})
console.log('fin')


