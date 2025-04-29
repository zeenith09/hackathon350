// add event listener
document.addEventListener("DOMContentLoaded", function () {
    /* This add-to-cart was AI generated using generic code and I edited it to work for our project */
    document.querySelectorAll(".add-button").forEach(button => {
        button.addEventListener("click", function () {
            let productId = this.getAttribute("data-product");

            fetch(`/cart/add/${productId}/`, {
                method: "GET",
                headers: {
                    "X-Requested-With": "XMLHttpRequest"
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.cart_count !== undefined) {
                    // Update cart count
                    document.querySelector(".shopping-cart .container-subtitle").textContent =
                        `${data.cart_count} product(s) in cart`;

                    // Optionally update cart list with a placeholder
                    const cartList = document.querySelector(".shopping-cart-list");
                    const newItem = document.createElement("li");
                    newItem.textContent = data.last_item;
                    newItem.classList.add("shopping-cart-item");
                    cartList.appendChild(newItem);
                }
            });
        });
    });
});