

const canvas = document.getElementById('canvas1') ;
const ctx = canvas.getContext('2d') ;
canvas.width = window.innerWidth ;
canvas.height = window.innerHeight ;
const particlesArray = [] ;
c = randomColor() ;


window.addEventListener('resize',function(){
    canvas.width = window.innerWidth ;
    canvas.height = window.innerHeight ;
});

const mouse = {
    x : undefined ,
    y : undefined ,
}


window.addEventListener('click',function(event){
    mouse.x = event.x ;
    mouse.y = event.y ;
    // console.log(event) ;
    // console.log(mouse) ;
    particlesArray.push(new Particle()) ;
}) ;

window.addEventListener('mousemove',function(event){
    mouse.x = event.x ;
    mouse.y = event.y ;
    particlesArray.push(new Particle()) ;
}) ;

function randomColor(){
    const colors = ['#fff','#f00','#0f0','#00f','#f0f','#ff0','#0ff','#099','#a0f'] ;
    i = parseInt(Math.random() * (colors.length) + 1)
    var color = colors[i] ;
    return color ;
}


class Particle {
    constructor(){
        this.x = mouse.x ;
        this.y = mouse.y ;
        // this.size = Math.random() * 5 + 1 ;
        this.h = Math.random() * 10 + 1 ;
        this.speedX = Math.random() * 2 - 2 ;
        this.speedY = Math.random() * 2 - 2 ;
    }
    update(){
         this.x += this.speedX ;
         this.y += this.speedY ;
        //  if(this.size > 0.1) this.size -= 0.1 ;
         if(this.h > 1) this.h -= 0.1 ;
    }
    draw(){
        ctx.fillStyle = c ;
        ctx.beginPath() ; 
        ctx.rect(this.x,this.y,this.h,this.h) ;
        // ctx.arc(this.x,this.y,this.h,this.w,0) ; 
        ctx.fill() ; 
    }
}

function handleParticles(){
    for(let i = 0;i < particlesArray.length;i++){
        particlesArray[i].update();
        particlesArray[i].draw() ;
        if(particlesArray[i].size <= 0.3){
            particlesArray.splice(i, 1) ;
            // console.log(particlesArray.length) ;
            i--;
        }
    }
}


function animate(){
    ctx.clearRect(0,0,canvas.width,canvas.height) ;
    handleParticles() ;
    requestAnimationFrame(animate) ;
}
animate() ;


