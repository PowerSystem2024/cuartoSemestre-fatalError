
        // Inicializar el carrito desde localStorage o como array vacío
        let cart = JSON.parse(localStorage.getItem('cart')) || [];

        // Elementos del DOM
        const shopContent = document.getElementById("shop-content");
        const modalContainer = document.getElementById("modal-container");
        const modalOverlay = document.getElementById("modal-overlay");
        const cartBtn = document.getElementById("cart-btn");
        const cartCounter = document.getElementById("cart-counter");

        // Mostrar productos en la tienda
        function displayProducts() {
            products.forEach(product => {
                const productCard = document.createElement("div");
                productCard.classList.add("card");
                productCard.innerHTML = `
                    <img src="${product.img}" alt="${product.productName}" class="product-img">
                    <div class="product-info">
                        <h3>${product.productName}</h3>
                        <p class="product-price">$${product.price.toFixed(2)}</p>
                        <button class="btn-add" data-id="${product.id}">Agregar al carrito</button>
                    </div>
                `;
                shopContent.appendChild(productCard);
            });

            // Agregar event listeners a los botones
            document.querySelectorAll('.btn-add').forEach(button => {
                button.addEventListener('click', (e) => {
                    const productId = parseInt(e.target.getAttribute('data-id'));
                    addToCart(productId);
                });
            });
        }

        // Agregar producto al carrito
        function addToCart(productId) {
            const product = products.find(p => p.id === productId);
            const existingProduct = cart.find(p => p.id === productId);
            
            if (existingProduct) {
                existingProduct.quanty++;
            } else {
                cart.push({...product});
            }
            
            updateCart();
            showNotification(`${product.productName} agregado al carrito`);
        }

        // Mostrar notificación
        function showNotification(message) {
            const notification = document.createElement('div');
            notification.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                background: #27ae60;
                color: white;
                padding: 15px 20px;
                border-radius: 5px;
                z-index: 1000;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            `;
            notification.textContent = message;
            document.body.appendChild(notification);
            
            setTimeout(() => {
                notification.style.opacity = '0';
                notification.style.transition = 'opacity 0.5s';
                setTimeout(() => notification.remove(), 500);
            }, 2000);
        }

        // Mostrar carrito
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
                                <p>Precio unitario: $${product.price.toFixed(2)}</p>
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
                modalFooter.innerHTML = `
                    <div class="total-price">Total: $${total.toFixed(2)}</div>
                    <button class="checkout-btn" id="checkout-btn">Pagar con MercadoPago</button>
                `;
                modalContainer.append(modalFooter);

                // INTEGRACIÓN CON MERCADOPAGO
                const checkoutBtn = document.getElementById("checkout-btn");
                checkoutBtn.addEventListener("click", async () => {
                    checkoutBtn.textContent = "Procesando...";
                    checkoutBtn.disabled = true;
                    
                    try {
                        // Crear preferencia de pago
                        const preference = {
                            items: cart.map(product => ({
                                title: product.productName,
                                quantity: product.quanty,
                                unit_price: product.price,
                                picture_url: product.img
                            })),
                            back_urls: {
                                success: window.location.href,
                                failure: window.location.href,
                                pending: window.location.href
                            },
                            auto_return: "approved"
                        };

                        // Enviar solicitud al servidor para crear preferencia
                        const response = await fetch('http://localhost:3000/create_preference', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify(preference)
                        });

                        const data = await response.json();

                        if (data.preference_id) {
                            // Redirigir a MercadoPago
                            window.location.href = data.preference_url;
                        } else {
                            console.error('Error al crear preferencia:', data.error);
                            alert('Error al procesar el pago. Intenta nuevamente.');
                        }
                    } catch (error) {
                        console.error('Error:', error);
                        alert('Error al conectar con el servidor de pagos. Asegúrate de que el servidor esté ejecutándose en http://localhost:3000');
                    } finally {
                        checkoutBtn.textContent = "Pagar con MercadoPago";
                        checkoutBtn.disabled = false;
                    }
                });

            } else {
                const modalText = document.createElement("h2");
                modalText.className = "empty-cart";
                modalText.innerText = "¡Tu carrito está vacío!";
                modalContainer.append(modalText);
            }
        };

        // Event listener para el botón del carrito
        cartBtn.addEventListener("click", displayCart);

        // Eliminar producto del carrito
        const deleteCartProduct = (id) => {
            const foundId = cart.findIndex(element => element.id === id);
            cart.splice(foundId, 1);
            updateCart();
        };

        // Mostrar contador del carrito
        const displayCartCounter = () => {
            const cartLength = cart.reduce((acc, el) => acc + el.quanty, 0);
            if (cartLength > 0) {
                cartCounter.style.display = "block";
                cartCounter.innerText = cartLength;
            } else {
                cartCounter.style.display = "none";
            }
        };

        // Actualizar carrito
        const updateCart = () => {
            // Guardar en localStorage
            localStorage.setItem('cart', JSON.stringify(cart));
            
            // Actualizar contador
            displayCartCounter();
            
            // Si el modal está abierto, actualizar la vista
            if (modalContainer.style.display === "block") {
                displayCart();
            }
        };

        // Inicializar la tienda
        displayProducts();
        displayCartCounter();