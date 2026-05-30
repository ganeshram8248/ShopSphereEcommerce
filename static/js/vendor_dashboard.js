document.addEventListener(

"DOMContentLoaded",

()=>{


/* Welcome text animation */

const title =

document.querySelector(

".navbar h1"

);


let text =

title.innerText;


title.innerText="";


let i=0;


function typing(){


if(i<text.length){

title.innerHTML +=

text.charAt(i);


i++;


setTimeout(

typing,

100

);

}


}


typing();




/* Count animation */

const nums=

document.querySelectorAll(

".box h1"

);



nums.forEach(

num=>{


let target=

parseInt(

num.innerText.replace(

/[^0-9]/g,

""

)

)||0;



let count=0;



function update(){


let speed=

Math.ceil(

target/50

);



count += speed;



if(

count<target

){

num.innerHTML=

count;


requestAnimationFrame(

update

);

}


else{


num.innerHTML=

target;


}



}



update();



}

);




/* Floating cards */

const cards=

document.querySelectorAll(

".box"

);



cards.forEach(

(card,index)=>{


card.style.opacity=

"0";


card.style.transform=

"translateY(50px)";



setTimeout(()=>{


card.style.transition=

".8s";


card.style.opacity=

"1";


card.style.transform=

"translateY(0)";


},

index*200



);



}

);




/* Live clock */

let clock=

document.createElement(

"div"

);



clock.classList.add(

"clock"

);



document.body.appendChild(

clock

);



setInterval(()=>{


clock.innerHTML=

"🕒 " +

new Date()

.toLocaleTimeString();


},1000);




/* Random glow effect */

setInterval(()=>{


cards.forEach(

card=>{


card.style.boxShadow=

"0 0 30px rgba(0,198,255,.8)";


setTimeout(()=>{


card.style.boxShadow=

"0 15px 30px rgba(0,0,0,.2)";


},1000);



}


);



},3000);





/* Mouse movement effect */

document.addEventListener(

"mousemove",

e=>{


document.body.style.background=

`radial-gradient(

circle at

${e.clientX}px

${e.clientY}px,

rgba(
0,
198,
255,
0.12
),

#0f172a

)`;


}



);



/* Verified seller animation */

let verified=

document.querySelector(

".verified"

);



if(

verified

){

setInterval(()=>{


verified.style.transform=

"scale(1.1)";


setTimeout(()=>{


verified.style.transform=

"scale(1)";


},500);


},1000);

}



});