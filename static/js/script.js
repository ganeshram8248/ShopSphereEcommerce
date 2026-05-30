let qty = 1;

function increaseQty(){

    qty++;

    document.getElementById("qty").innerHTML = qty;
}

function decreaseQty(){

    if(qty > 1){

        qty--;

        document.getElementById("qty").innerHTML = qty;
    }
}

const searchInput =
document.getElementById("searchInput");

if(searchInput){

    searchInput.addEventListener("keyup", function(){

        let filter =
        searchInput.value.toUpperCase();

        let cards =
        document.querySelectorAll(".product-card");

        cards.forEach(card => {

            let title =
            card.querySelector("h2")
            .innerText.toUpperCase();

            if(title.indexOf(filter) > -1){

                card.style.display = "";

            }else{

                card.style.display = "none";
            }

        });

    });

}