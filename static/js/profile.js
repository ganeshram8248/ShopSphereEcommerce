console.log("profile.js loaded");

document.addEventListener("DOMContentLoaded", function () {

    const editBtn = document.getElementById("editBtn");
    const editForm = document.getElementById("editForm");

    if (editBtn && editForm) {

        editBtn.addEventListener("click", function () {

            if (editForm.style.display === "none" || editForm.style.display === "") {
                editForm.style.display = "block";
            } else {
                editForm.style.display = "none";
            }

        });

    } else {
        console.log("Button or Form not found");
    }

});