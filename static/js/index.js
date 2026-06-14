alert("JS Loaded");

document.getElementById("searchBtn").onclick = function () {

    let text =
        document.getElementById("searchInput")
        .value
        .toLowerCase();

    let cards =
        document.getElementsByClassName("card");

    for (let i = 0; i < cards.length; i++) {

        let name =
            cards[i]
            .getElementsByTagName("h2")[0]
            .innerText
            .toLowerCase();

        if (name.indexOf(text) > -1) {

            cards[i].style.display = "";

        } else {

            cards[i].style.display = "none";

        }

    }

};