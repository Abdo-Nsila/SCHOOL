const box = document.getElementById('video');
box.style.position = 'absolute';

document.addEventListener("mousemove", logKey);
function logKey(e) {

    box.style.top = e.clientY - 175 +'px';
    box.style.left = e.clientX - 310 + 'px';

    box.style.scale = (0.002 * e.clientX) ; 
    box.style.borderRadius = (e.clientY / 10) + '%' ;    

}