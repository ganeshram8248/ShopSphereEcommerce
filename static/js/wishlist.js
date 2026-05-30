document.addEventListener(

"DOMContentLoaded",

function(){

updateCount();



let search =

document.getElementById(
"search"
);


search.addEventListener(

"keyup",

function(){


let value =

this.value.toLowerCase();



let cards =

document.querySelectorAll(
".wishlist-card"
);



cards.forEach(

function(card){


let name =

card.querySelector(
"h3"
)

.innerText

.toLowerCase();



if(

name.includes(
value
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

);


}





);





function removeItem(

btn,
wishlistId

){


let card =

btn.closest(
".wishlist-card"
);



card.style.transform=

"scale(0)";



card.style.opacity=

"0";



setTimeout(

function(){

card.remove();

updateCount();

},

400

);




fetch(

"/remove-wishlist/"+

wishlistId+

"/",

{

method:"POST",


headers:{


"X-CSRFToken":

getCookie(
"csrftoken"
)

}


}


)



.then(

response=>

response.json()

)

.then(

data=>{

console.log(
data
);

}

)



.catch(

error=>{

console.log(
error
);

}

);



}




function updateCount(){


let total =

document.querySelectorAll(

".wishlist-card"

).length;



document.getElementById(

"wishlistCount"

).innerText=

total;


}




function getCookie(

name

){


let cookieValue =

null;



if(

document.cookie &&

document.cookie !== ""

){


let cookies =

document.cookie.split(
";"
);



for(

let i=0;

i<cookies.length;

i++

){


let cookie =

cookies[i]

.trim();



if(

cookie.substring(

0,

name.length+1

)

===

(name+"=")

){


cookieValue =

decodeURIComponent(

cookie.substring(

name.length+1

)

);



break;


}



}



}



return cookieValue;



}