var btn = document.querySelector("#btn") ;
console.log(btn) ;
w = window.innerWidth ;
h = window.innerHeight ;

// window.addEventListener('mousemove',function(event){
//     x = event.x ;
//     y = event.y ;
//     console.log(x,y) ;
// }) ;

function hrb(){
    text = 
    // y = Math.random() * 100 + 50 ;
    // btn.style.top = `${y}px` ;
    x = Math.random() * 500 + 50 ;
    btn.style.left = `${x}px` ;
}
var str = "abdo.gmail.com";
if (str.match(/[^gmail.com]/)){
    console.log(true) ;
}
else{
    console.log(false) ;
}
// if (str.match(/[^a-zA-Z0-9]/)) {
     // contains illegal characters
// }
