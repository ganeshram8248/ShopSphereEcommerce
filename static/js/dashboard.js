window.onload=

function(){


document

.querySelectorAll(

".card"

)

.forEach(

card=>{


card.addEventListener(

"mouseenter",

function(){

this.style.transform=

"scale(1.05)";

}


);



card.addEventListener(

"mouseleave",

function(){

this.style.transform=

"scale(1)";

}


);


}

);



}






document

.querySelector(

".banner button"

)

.addEventListener(

"click",

function(){


window.location.href=

"/products";


}


);