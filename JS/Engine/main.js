const canvas = document.querySelector("#canvas");
const c = canvas.getContext("2d");

canvas.width = 850;
canvas.height = 720;

c.fillRect(0, 0, canvas.width, canvas.height);

const gravity = 0.7;

const player = new Fighter({
  position: { x: 150, y: 0 },
  velocity: { x: 0, y: -5 },
  color: "red",
});


function animate() {
  window.requestAnimationFrame(animate);
  c.fillStyle = "#000";

  c.fillRect(0, 0, canvas.width, canvas.height);
  player.update();
}
animate();

