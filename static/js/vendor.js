document
.querySelectorAll(
".card"
)

.forEach(

card=>{

card.addEventListener(

"mouseover",

function(){

this.style.transform=

"scale(1.05)"

}

);


card.addEventListener(

"mouseout",

function(){

this.style.transform=

"scale(1)"

}

);

}

);



document.querySelector(

".top button"

)

.addEventListener(

"click",

function(){

window.location=

"/add-product/"

}

);