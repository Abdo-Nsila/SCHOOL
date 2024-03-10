function randomNumber(){
    const num = Math.floor(Math.random()*100000)
    return  num
}
const rolit = document.querySelector(".all")
const btn = document.querySelector(".btn")
btn.addEventListener("click",e =>{
    rolit.style.setProperty("rotate", `${randomNumber()}deg`)
})




