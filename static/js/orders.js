function cancelOrder(id) {

    if (!confirm("Are you sure to cancel this order?")) return;

    fetch("/cancel/" + id + "/", {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        }
    })
    .then(res => res.json())
    .then(data => {

        if (data.success) {
            alert("Order Cancelled");
            location.reload();
        } else {
            alert("Something went wrong");
        }

    });

}

// CSRF TOKEN
function getCookie(name) {
    let cookieValue = null;

    document.cookie.split(";").forEach(c => {
        c = c.trim();

        if (c.startsWith(name + "=")) {
            cookieValue = decodeURIComponent(c.split("=")[1]);
        }
    });

    return cookieValue;
}