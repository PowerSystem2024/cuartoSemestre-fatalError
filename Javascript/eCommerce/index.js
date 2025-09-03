const shopContent = document.getElementById('shop-content');
const cart = [];

products.forEach(product => {
    const productCard = document.createElement('div');
    productCard.classList.add('product-card');

    productCard.innerHTML = `
        <img src="${product.image}" alt="${product.name}">
        <h3>${product.name}</h3>
        <p>$${product.price.toFixed(2)}</p>
    `;

    // Agrego la card al contenedor
    shopContent.append(productCard);

    // Botón comprar
    const buyButton = document.createElement("button");
    buyButton.innerText = "Comprar";

    // Agrego el botón dentro de la card
    productCard.append(buyButton);

    buyButton.addEventListener("click", () => {
        const repeat = cart.some(repeatProduct => repeatProduct.id === product.id);
        if(repeat){
            cart.map(prod => {
                if(prod.id === product.id) {
                    prod.quanty++;
                }
            });
        } else {
            cart.push({
                id: product.id,
                productName: product.name,
                price: product.price,
                quanty: 1,
                img: product.image
            });
        }
        console.log(cart);
    });
});
