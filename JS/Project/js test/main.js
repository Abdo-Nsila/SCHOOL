var snake = document.getElementById("snake") ;


function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

Tab = [0,0];

async function tr_Up(index,plus) {
    for (var i = 0 ; i < 1 ; i++) {
        Tab[index] += plus
        snake.style.top = String(Tab[index])+"px";
        // console.log(i);
        // await sleep(50);
    }
}
async function tr_Down(index,plus) {
    for (var i = 0 ; i < 1 ; i++) {
        Tab[index] -= plus
        snake.style.top = String(Tab[index])+"px";
        // console.log(i);
        // await sleep(50);
    }
}


async function tr_Right(index,plus) {
    for (var i = 0 ; i < 1 ; i++) {
        Tab[index] += plus
        snake.style.right = String(Tab[index])+"px";
        // console.log(i);
        // await sleep(50);
    }
}
async function tr_Left(index,plus) {
    for (var i = 0 ; i < 1 ; i++) {
        Tab[index] -= plus
        snake.style.right = String(Tab[index])+"px";
        // console.log(i);
        // await sleep(50);
    }
}




// tr_Up()
// tr_Down()
// tr_Right()



window.addEventListener("keyup",checkKeyPress,false)
function checkKeyPress(key){
    if (key.keyCode == "39"){
        add_l = 10
        add_r = 0
        add_b = 0
        add_t = 0
    }
    if (key.keyCode == "40"){
        loop(0,10,0,0)
    }
    if (key.keyCode == "37"){
        loop(0,0,10,0)
    }
    if (key.keyCode == "38"){
        loop(0,10,0,0)
    }

}
function loop(add_l,add_b,add_r,add_t){
    while(true){
        tr_Left(0,add_l)
        tr_Up(1,add_t)
        tr_Right(0,add_r)
        tr_Down(1,add_b)

}}
