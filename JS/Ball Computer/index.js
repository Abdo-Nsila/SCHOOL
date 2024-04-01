// Get the canvas and its 2D context
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// Get the audio element
const bounceSound = new Audio("./audio/dandan.mp3");

let isGameStarted = false;
canvas.width = innerWidth;
canvas.height = innerHeight;
const CANVAS_BACKGROUND = "rgb(43, 43, 43, 0.5)";
const GRAVITY = 0.1;
const BORDER_WIDTH = 2;
let hsl = 0;

// Define a flag to track whether the ball is touching the circle
let isTouchingCircle = false;

// Define the circle properties
const circle = {
  x: canvas.width / 2,
  y: canvas.height / 2,
  radius: 300,
};

// Define the ball properties
const ball = {
  x: circle.x,
  y: circle.y - circle.radius + 20, // Initial position inside the circle
  radius: 10,
  speedX: Math.random() * 25 + 15, // Random initial speed in x direction
  speedY: Math.random() * 25 + 15, // Random initial speed in y direction
  volacity: 1,
  gravity: GRAVITY, // Gravity value
};

// Create a new instance of the Lines class
const lines = new Lines();

// Function to draw the circle
function drawCircle() {
  ctx.strokeStyle = `hsl(${hsl}, 100%, 50%)`;
  ctx.lineWidth = BORDER_WIDTH;
  ctx.beginPath();
  ctx.arc(circle.x, circle.y, circle.radius, 0, Math.PI * 2);
  ctx.stroke();
}

// Function to draw the ball
function drawBall() {
  // ctx.fillStyle = `hsl(${hsl}, 100%, 50%)`;
  ctx.fillStyle = "white";
  ctx.beginPath();
  ctx.arc(ball.x, ball.y, ball.radius, 0, Math.PI * 2);
  ctx.fill();
}

// Function to update the ball's position
function update() {
  // Update ball's position with gravity effect
  ball.speedY += ball.gravity;
  ball.x += ball.speedX;
  ball.y += ball.speedY;

  // Check collision with circle boundary
  const dx = ball.x - circle.x;
  const dy = ball.y - circle.y;
  const distance = Math.sqrt(dx * dx + dy * dy);

  if (distance > circle.radius - ball.radius) {
    // Collision detected, adjust ball's position and speed
    // const angle = Math.atan2(dy, dx);
    const angle = Math.atan2(dy, dx);
    ball.x = circle.x + Math.cos(angle) * (circle.radius - ball.radius);
    ball.y = circle.y + Math.sin(angle) * (circle.radius - ball.radius);
    // Reflect the ball's speed
    const normalX = Math.cos(angle);
    const normalY = Math.sin(angle);
    const dot = ball.speedX * normalX + ball.speedY * normalY;
    if (ball.volacity < 1.06) {
      ball.volacity += 0.001
      ball.speedX = (ball.speedX - 2 * dot * normalX) * ball.volacity;
      ball.speedY = (ball.speedY - 2 * dot * normalY) * ball.volacity;
    } else {
      ball.speedX = ball.speedX - 2 * dot * normalX;
      ball.speedY = ball.speedY - 2 * dot * normalY;
    }

    // Update the flag to indicate that the ball is touching the circle
    isTouchingCircle = true;
  } else {
    // Update the flag to indicate that the ball is not touching the circle
    isTouchingCircle = false;
  }

  // Control audio playback based on whether the ball is touching the circle
  if (isTouchingCircle) {
    console.log("Touch Done");
    //! Increase the ball's radius when touching the circle
    ball.radius += 2;
    // if (ball.radius < circle.radius / 1.5) {
    //   ball.radius += 2;
    // }
    bounceSound.play();
    setTimeout(() => {
      //! Lines draw();
      const angle = Math.atan2(dy, dx);
      //* Get Ball Center & Touch Point
      const ballCenter = { x: ball.x, y: ball.y };
      const touchPoint = {
        x: circle.x + Math.cos(angle) * circle.radius,
        y: circle.y + Math.sin(angle) * circle.radius,
      };
      const line = new Line(touchPoint, ballCenter);
      lines.lines.push(line);
      bounceSound.pause();
    }, 150);
  }
}

// Function to clear the canvas and redraw everything
function draw() {
  hsl = (hsl + 1) % 360;
  ctx.fillStyle = CANVAS_BACKGROUND;
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  // lines.draw();
  drawCircle();
  drawBall();
}

// Game loop
function gameLoop() {
  update();
  draw();
  requestAnimationFrame(gameLoop);
}

// Start the game loop
gameLoop();
