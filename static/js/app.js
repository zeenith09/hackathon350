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

                    const tableBody = document.querySelector(".shopping-cart-contents tbody");
                    if (data.new_item) {
                        const newRow = document.createElement("tr");
                        newRow.innerHTML = `
                            <td>${data.name}</td>
                            <td>$${data.price}</td>
                            <td>${data.quantity}</td>
                        `;
                        tableBody.appendChild(newRow);
                    }
                    else {
                        const tableRows = document.querySelectorAll(".shopping-cart-contents tbody tr");
                        tableRows.forEach(row => {
                            const tableRowTds = row.querySelectorAll("td");
                            if (tableRowTds[0].textContent == data.name) {
                                tableRowTds[2].textContent = data.quantity;
                            }
                        })
                    }
                }
            });
        });
    });
});