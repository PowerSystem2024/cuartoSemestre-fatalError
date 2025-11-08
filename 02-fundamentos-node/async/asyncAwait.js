async function hola(nombre) {
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
            console.log('hola' + nombre)
            resolve(nombre)
        }, 1000)
    });
}

async function hablar (nombre){
    return new Promise ((resolve, reject) => {
        setTimeout(function() {
            console.log('hablando')
            resolve();
        }, 1000)
    });
}

async function adios(mensaje){
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
            console.log('adios' + nombre)
            //resolve();
            reject("hay un error");
        }, 1000)
    });
}

//await hola('Ariel'); // esto es una mala sintaxis

async function main(params) {
    let nombre = await hola('Luca');
    await hablar();
    await hablar();
    await hablar();
    await adios(nombre);
    console.log('Terminamos el proceso..')
}
console.log('Empezamos el proceso...')
main();
console.log('Esta va a ser la segunda instruccion')
