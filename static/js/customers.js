// SEARCH FUNCTION
function searchCustomer() {
    let input = document.getElementById("search").value.toLowerCase();
    let cards = document.querySelectorAll(".customer-card");

    cards.forEach(card => {
        let name = card.querySelector(".name").innerText.toLowerCase();

        if (name.includes(input)) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
}

// VIEW PROFILE
function viewProfile(username) {
    alert("Opening profile of: " + username);
    window.location.href = "/profile/" + username + "/";
}