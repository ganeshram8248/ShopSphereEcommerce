function searchProduct(){

let input =

document
.getElementById(
"searchInput"
)

.value

.toLowerCase();



let cards=

document

.querySelectorAll(

".card"

);



cards.forEach(

function(card){

let text=

card.innerText

.toLowerCase();



if(

text.includes(
input
)

){

card.style.display=

"block";

}


else{

card.style.display=

"none";

}


}

);

}



function filterProduct(

category

){


let cards=

document.querySelectorAll(

".card"

);



cards.forEach(

function(card){


if(

category==="all"

||

card.classList.contains(

category

)

){

card.style.display=

"block";

}


else{


card.style.display=

"none";


}


});


}



document

.querySelectorAll(

".card"

)

.forEach(

(card,index)=>{


card.style.opacity="0";


setTimeout(

()=>{


card.style.opacity="1";


card.style.transition=

"0.5s";


},

index*100

);


});