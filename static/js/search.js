let qty = 1;

function increaseQty() {
    qty++;
    const qtyEl = document.getElementById("qty");
    if (qtyEl) qtyEl.innerHTML = qty;
}

function decreaseQty() {
    if (qty > 1) {
        qty--;
        const qtyEl = document.getElementById("qty");
        if (qtyEl) qtyEl.innerHTML = qty;
    }
}

const searchInput = document.getElementById("searchInput");
const searchBtn = document.getElementById("searchBtn");

function filterProducts() {
    const input = searchInput ? searchInput.value.toUpperCase() : "";
    const cards = document.querySelectorAll(".product-card");

    cards.forEach(card => {
        const titleEl = card.querySelector("h2");
        if (!titleEl) return;

        const title = titleEl.innerText.toUpperCase();
        card.style.display = title.includes(input) ? "" : "none";
    });
}

if (searchInput) {
    searchInput.addEventListener("keyup", filterProducts);
}

if (searchBtn) {
    searchBtn.addEventListener("click", filterProducts);
}