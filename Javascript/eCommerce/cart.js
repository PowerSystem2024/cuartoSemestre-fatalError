const modalContainer = document.getElementById('modal-container');
const modalOverlay = document.getElementById('modal-overlay');
const cartBtn = document.getElementById('cart-btn');

const displayCart = () => {
    // limpiar modal
    modalContainer.innerHTML = "";
    modalOverlay.style.display = "block";
    modalContainer.style.display = "block";

    // HEADER
    const modalHeader = document.createElement("div");
    modalHeader.className = "modal-header";

    const modalClose = document.createElement("div");
    modalClose.innerText = "❌";
    modalClose.className = "modal-close";

    // evento cerrar
    modalClose.addEventListener("click", () => {
        modalContainer.style.display = "none";
        modalOverlay.style.display = "none";
    });

    modalHeader.append(modalClose);

    const modalTitle = document.createElement("div");
    modalTitle.innerText = "Carrito";
    modalTitle.className = "modal-title";

    modalHeader.append(modalTitle);
    modalContainer.append(modalHeader);

    // LISTA DE PRODUCTOS
    cart.forEach(product => {
        const productCart = document.createElement("div");
        productCart.className = "modal-product";
        productCart.innerHTML = `
            <img src="${product.img}" alt="${product.productName}">
            <h3>${product.productName}</h3>
            <p>$${product.price}</p>
            <p>Cantidad: ${product.quanty}</p>
        `;
        modalContainer.append(productCart);
    });

    // TOTAL
    const total = cart.reduce((acc, el) => acc + el.price * el.quanty, 0);

    const totalContainer = document.createElement("div");
    totalContainer.className = "modal-total";
    totalContainer.innerText = `Total: $${total}`;

    modalContainer.append(totalContainer);
};

cartBtn.addEventListener("click", displayCart);

