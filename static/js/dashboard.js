// ===============================
// CUSTOMER SEARCH FILTER
// ===============================

document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.getElementById("search");
    const cards = document.querySelectorAll(".customer-card");

    if (!searchInput) return;

    searchInput.addEventListener("input", function () {

        const query = searchInput.value.toLowerCase().trim();

        cards.forEach(card => {

            const name = card.querySelector(".name")?.innerText.toLowerCase() || "";
            const phone = card.querySelector("p")?.innerText.toLowerCase() || "";
            const role = card.querySelector(".premium")?.innerText.toLowerCase() || "";

            if (
                name.includes(query) ||
                phone.includes(query) ||
                role.includes(query)
            ) {
                card.style.display = "block";
            } else {
                card.style.display = "none";
            }
        });
    });

});


// ===============================
// VIEW PROFILE BUTTON (OPTIONAL)
// ===============================

document.addEventListener("click", function (e) {

    if (e.target && e.target.innerText === "View Profile") {

        const card = e.target.closest(".customer-card");

        const name = card.querySelector(".name").innerText;

        alert("Opening profile of: " + name);

        // You can redirect later:
        // window.location.href = "/customer/" + name + "/";
    }
});