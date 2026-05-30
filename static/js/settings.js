// TAB SWITCHING
function openTab(tabName) {

    let tabs = document.querySelectorAll(".tab-content");
    let buttons = document.querySelectorAll(".tab");

    tabs.forEach(t => t.classList.remove("active"));
    buttons.forEach(b => b.classList.remove("active"));

    document.getElementById(tabName).classList.add("active");

    event.target.classList.add("active");
}


// SAVE ANIMATION (demo)
function saveSettings() {
    let toast = document.getElementById("toast");

    toast.style.display = "block";

    setTimeout(() => {
        toast.style.display = "none";
    }, 2000);
}