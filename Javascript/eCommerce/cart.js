const modalContainer = document.getElementById("modal-container");
const modalOverlay = document.getElementById("modal-overlay");
const cartBtn = document.getElementById("cart-btn");
const cartCounter = document.getElementById("cart-counter");

const displayCart = () => {
    modalContainer.innerHTML = "";
    modalOverlay.style.display = "block";
    modalContainer.style.display = "block";

    // HEADER
    const modalHeader = document.createElement("div");
    modalHeader.className = "modal-header";

    const modalClose = document.createElement("div");
    modalClose.className = "modal-close";
    modalClose.innerText = "✖"; 
    modalClose.addEventListener("click", () => {
        modalContainer.style.display = "none";
        modalOverlay.style.display = "none";
    });

    const modalTitle = document.createElement("div");
    modalTitle.className = "modal-title";
    modalTitle.innerText = "Carrito";

    modalHeader.append(modalTitle, modalClose);
    modalContainer.append(modalHeader);

    // BODY
    if (cart.length > 0) {
        cart.forEach((product) => {
            const modalBody = document.createElement("div");
            modalBody.className = "modal-body";
            modalBody.innerHTML = `
                <div class="product">
                    <img class="product-img" src="${product.img}" alt="${product.productName}" />
                    <div class="product-info">
                        <h4>${product.productName}</h4>
                    </div>
                    <div class="quantity">
                        <span class="quantity-btn-decrease">-</span>
                        <span class="quantity-input">${product.quanty}</span>
                        <span class="quantity-btn-increase">+</span>
                    </div>
                    <div class="price">${(product.price * product.quanty).toFixed(2)} $</div>
                    <div class="delete-product">X</div>
                </div>
            `;
            modalContainer.append(modalBody);

            const decrease = modalBody.querySelector(".quantity-btn-decrease");
            const increase = modalBody.querySelector(".quantity-btn-increase");

            decrease.addEventListener("click", () => {
                if (product.quanty > 1) product.quanty--;
                updateCart(); 
            });

            increase.addEventListener("click", () => {
                product.quanty++;
                updateCart(); 
            });

            const deleteButton = modalBody.querySelector(".delete-product");
            deleteButton.addEventListener("click", () => {
                deleteCartProduct(product.id);
            });
        });

        // FOOTER
        const total = cart.reduce((acc, el) => acc + el.price * el.quanty, 0);
        const modalFooter = document.createElement("div");
        modalFooter.className = "modal-footer";
        modalFooter.innerHTML = `<div class="total-price">Total: $${total.toFixed(2)}</div>`;
        modalContainer.append(modalFooter);
    } else {
        const modalText = document.createElement("h2");
        modalText.className = "modal-body";
        modalText.innerText = "¡Tu carrito está vacío!";
        modalContainer.append(modalText);
    }
};

cartBtn.addEventListener("click", displayCart);

const deleteCartProduct = (id) => {
    const foundId = cart.findIndex(element => element.id === id);
    cart.splice(foundId, 1);
    updateCart();
};

const displayCartCounter = () => {
    const cartLength = cart.reduce((acc, el) => acc + el.quanty, 0);
    if (cartLength > 0) {
        cartCounter.style.display = "block";
        cartCounter.innerText = cartLength;
    } else {
        cartCounter.style.display = "none";
    }
};

const updateCart = () => {
    displayCart();
    displayCartCounter();
};
