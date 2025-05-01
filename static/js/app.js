// add event listener
document.addEventListener("DOMContentLoaded", function () {
    /* This add-to-cart was AI generated using generic code and I edited it to work for our project */
    
    // Add to cart button
    const addToCartBtn = document.getElementById("add-to-cart-btn");
    if (addToCartBtn) {
        addToCartBtn.addEventListener("click", function () {
            const selectedProduct = document.querySelector('input[name="product_id"]:checked');
            if (selectedProduct) {
                const productId = selectedProduct.value;
                addToCart(productId);
            } else {
                alert("Please select a product to add to cart");
            }
        });
    }

    // Remove from cart button
    const removeFromCartBtn = document.getElementById("remove-from-cart-btn");
    if (removeFromCartBtn) {
        removeFromCartBtn.addEventListener("click", function () {
            const selectedItem = document.querySelector('input[name="remove_item"]:checked');
            if (selectedItem) {
                const itemId = selectedItem.value;
                removeFromCart(itemId);
            } else {
                alert("Please select an item to remove from cart");
            }
        });
    }

    // Checkout button
    const checkoutBtn = document.getElementById("checkout-btn");
    if (checkoutBtn) {
        checkoutBtn.addEventListener("click", function () {
            window.location.href = "/checkout/";
        });
    }

    function addToCart(productId) {
        fetch(`/cart/add/${productId}/`, {
            method: "GET",
            headers: {
                "X-Requested-With": "XMLHttpRequest"
            }
        })
            .then(response => response.json())
            .then(data => {
                if (data.cart_count !== undefined) {
                    // Check if we need to remove the empty cart message
                    const emptyMessage = document.getElementById("empty-cart-message");
                    if (emptyMessage) {
                        emptyMessage.remove();
                    }

                    // Add new item or update quantity
                    const cartItemsList = document.getElementById("cart-items");
                    const existingItem = document.getElementById(`cart-item-${data.id}`);

                    if (!existingItem) {
                        // Create new item
                        const newItem = document.createElement("li");
                        newItem.id = `cart-item-${data.id}`;
                        newItem.innerHTML = `
                        <label>
                            <input type="radio" name="remove_item" value="${data.id}" class="cart-radio">
                            ${data.name} - $${data.price} (Qty: ${data.quantity})
                        </label>
                    `;
                        cartItemsList.appendChild(newItem);
                    } else {
                        // Update quantity
                        const itemText = existingItem.querySelector("label");
                        itemText.innerHTML = `
                        <input type="radio" name="remove_item" value="${data.id}" class="cart-radio">
                        ${data.name} - $${data.price} (Qty: ${data.quantity})
                    `;
                    }

                    // Uncheck the product radio button
                    const selectedProduct = document.querySelector('input[name="product_id"]:checked');
                    if (selectedProduct) {
                        selectedProduct.checked = false;
                    }
                }
            })
            .catch(error => {
                console.error("Error adding to cart:", error);
            });
    }

    function removeFromCart(itemId) {
        fetch(`/cart/remove/${itemId}/`, {
            method: "GET",
            headers: {
                "X-Requested-With": "XMLHttpRequest"
            }
        })
            .then(response => response.json())
            .then(data => {
                if (data.message === "Item removed") {
                    // Remove the item from the cart list
                    const itemToRemove = document.getElementById(`cart-item-${itemId}`);
                    if (itemToRemove) {
                        itemToRemove.remove();
                    }

                    // If cart is now empty, add the empty message
                    if (data.cart_count === 0) {
                        const cartItemsList = document.getElementById("cart-items");
                        const emptyMessage = document.createElement("li");
                        emptyMessage.id = "empty-cart-message";
                        emptyMessage.textContent = "Your cart is empty!";
                        cartItemsList.appendChild(emptyMessage);
                    }
                }
            })
            .catch(error => {
                console.error("Error removing from cart:", error);
            });
    }
});
