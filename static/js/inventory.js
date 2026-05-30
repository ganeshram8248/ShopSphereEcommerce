// Search

document

.getElementById(

"search"

)

.addEventListener(

"keyup",

function(){


let value=

this.value

.toLowerCase();



document

.querySelectorAll(

".inventory-card"

)

.forEach(

card=>{


let name=

card.querySelector(

".name"

)

.innerText

.toLowerCase();



card.style.display=

name.includes(

value

)

?

"block"

:

"none";


}

);

}

);






function increase(

btn

){


let stock=

btn

.parentElement

.parentElement

.querySelector(

".stock"

);



stock.innerText=

parseInt(

stock.innerText

)

+1;


}





function decrease(

btn

){


let stock=

btn

.parentElement

.parentElement

.querySelector(

".stock"

);



if(

stock.innerText>0

){

stock.innerText=

parseInt(

stock.innerText

)

-1;

}


}





document

.querySelectorAll(

".update"

)

.forEach(

btn=>{


btn.addEventListener(

"click",

function(){

alert(

"Stock Updated"

);

}

);


}

);