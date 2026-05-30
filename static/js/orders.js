// TRACK ORDER (simple demo page redirect or popup)
function trackOrder(orderId) {
    alert("Tracking Order ID: " + orderId);
    // OR redirect:
    // window.location.href = "/track-order/" + orderId + "/";
}


// CANCEL ORDER (AJAX to Django)
function cancelOrder(orderId, btn) {

    if (!confirm("Are you sure you want to cancel this order?")) {
        return;
    }

    fetch("/cancel-order/" + orderId + "/", {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        }
    })
    .then(res => res.json())
    .then(data => {

        if (data.success) {
            btn.closest(".order-card").querySelector(".status").innerText = "Cancelled";
            btn.disabled = true;
            btn.innerText = "Cancelled";
            btn.style.background = "gray";
        }

    });
}


// CSRF helper
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}