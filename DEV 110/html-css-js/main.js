let stars = document.getElementById('stars');
let moon = document.getElementById('moon');
let mountains3 = document.getElementById('mountains3');
let mountains4 = document.getElementById('mountains4');
let river = document.getElementById('river');
let boat = document.getElementById('boat');


window.onscroll = function(){
    let value = scrollY;
    stars.style.left = value + 'px';
    moon.style.top = value  * 1.5 + 'px';
    mountains3.style.top = value  * 1.3 + 'px';
    mountains4 .style.top = value  * 1.3  + 'px';
    river.style.top = value + 'px';
    boat.style.top = value  + 'px';
    boat.style.left = value * 3 + 'px';
    }
