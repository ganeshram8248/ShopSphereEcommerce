let form = document.querySelector(
"form"
);

form.addEventListener(

"submit",

function(){

let pass =

document.querySelector(

'input[name="password"]'

).value;


if(pass.length<6){

alert(

"Password minimum 6 characters"

);

event.preventDefault();

}


let btn =

document.querySelector(
"button"
);

btn.innerHTML =

"Creating...";

}

);