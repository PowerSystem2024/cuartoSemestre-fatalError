function hola(nombre) {
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
            console.log('hola' + nombre)
            resolve(nombre)
        }, 1000)
    });
}

function hablar (nombre){
    return new Promise ((resolve, reject) => {
        setTimeout(function() {
            console.log('hablando')
            resolve();
        }, 1000)
    });
}

function adios(mensaje){
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
            console.log('adios' + nombre)
            //resolve();
            reject("hay un error");
        }, 1000)
})


// llamamos a la funcion
hola('Luca')
    .then(hablar)
    .then(adios)
    .then((nombre) =>{
        console.log("terminamos la promesa");
    })
    .catch(error => {
        console.log("Ha habido un error: ");
        console.log(error);
    })
    }