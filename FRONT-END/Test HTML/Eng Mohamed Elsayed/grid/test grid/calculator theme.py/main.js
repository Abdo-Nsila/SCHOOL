text = document.getElementById("display")
let n

var num = '';
function fct1(){
    num += "1"
    console.log(num);
    nbr = Number(num) + 1
    console.log(text.innerHTML)
    text.innerHTML = num;
}

let plus = "+"
function fctSum(){
    num += "+"
    console.log(num);
    nbr = Number(num) + 1
    console.log(text.innerHTML)
    text.innerHTML = num;
}



