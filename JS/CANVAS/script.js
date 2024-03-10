const canvas = document.getElementById('canvas1') ;
const ctx = canvas.getContext('2d') ;
canvas.width = window.innerWidth ;
canvas.height = window.innerHeight ;
const particlesArray = [] ;
let hue = 0 ;
sound = new Audio('click2.mp3') ;


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
    for(let i=0;i<1;i++){
        particlesArray.push(new Particle()) ;
    }
}) ;

window.addEventListener('mousemove',function(event){
    mouse.x = event.x ;
    mouse.y = event.y ;
    for(let i=0;i<1;i++){
        particlesArray.push(new Particle()) ;
    }
}) ;


class Particle {
    constructor(){
        this.x = mouse.x ;
        this.y = mouse.y ;
        this.size = Math.random() * 10 + 1 ;
        this.speedX = Math.random() * 3 - 1.5 ;
        this.speedY = Math.random() * 3  - 1.5 ;
        this.color = `hsl(${hue},100%,50%)` ;
    }
    update(){
         this.x += this.speedX ;
         this.y += this.speedY ;
         if(this.size > 0.1) this.size -= 0.1 ;
    }
    draw(){
        ctx.fillStyle =  this.color ;
        ctx.beginPath() ; 
        ctx.arc(this.x,this.y,this.size,0,Math.PI * 2) ; 
        ctx.fill() ; 
    }
}


function handleParticles(){
    for(let i = 0;i < particlesArray.length;i++){
        particlesArray[i].update();
        particlesArray[i].draw() ;
        for(let j = i;j < particlesArray.length;j++){
            const dx = particlesArray[i].x - particlesArray[j].x ;
            const dy = particlesArray[i].y - particlesArray[j].y ;
            const distance = Math.sqrt(dx * dx + dy * dy) ;
            if(distance < 80){
                ctx.beginPath() ;
                ctx.strokeStyle = particlesArray[i].color ;
                ctx.lineWidth = 1 ;
                ctx.moveTo(particlesArray[i].x , particlesArray[i].y) ;
                ctx.lineTo(particlesArray[j].x , particlesArray[j].y) ;
                ctx.stroke() ;
                ctx.closePath() ;
            } 
        }
        if(particlesArray[i].size <= 0.3){
            particlesArray.splice(i, 1) ;
            // console.log(particlesArray.length) ;
            i--;
        }
    }
}


function animate(){
    // ctx.clearRect(0,0,canvas.width,canvas.height) ;
    ctx.fillStyle = 'rgba(0,0,0,0.2)' ;
    ctx.fillRect(0,0,canvas.width,canvas.height) ;
    handleParticles() ;
    hue += 2 ;
    requestAnimationFrame(animate) ;
}
animate() ;
