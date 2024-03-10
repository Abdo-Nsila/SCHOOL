const canvas = document.querySelector("canvas");
const c = canvas.getContext("2d");
//!---------------------- Settings -----------------------
canvas.width = innerWidth;
canvas.height = innerHeight;
const CURSEUR = {
  MouseX: 0,
  MouseY: 0,
  sensitivity: 1,
  size: 20,
  DISTANCE: 0,
};
let COMBO = 1;
let hsl = Math.floor(Math.random() * (200 - 0 + 1) + 0);
let score = 0;
const CANVAS_BACKGROUND = "rgb(43, 43, 43)";
const CERCLE_RADIUS = 60;
const APPROCH_RADIUS = CERCLE_RADIUS * 2;
const APPROCH_SPEED = 4;
const BORDER_WIDTH = 5;
const BORDER_COLOR = "white";
const FONT_SIZE = CERCLE_RADIUS - CERCLE_RADIUS / 3;

//!--------------- Slide Class -----------------
class Slide extends Cercle {
  constructor({
    startPoints,
    ctp1,
    ctp2,
    endPoints,
    x,
    y,
    radius,
    color,
    approchRadius,
    approchSpeed,
    velocity,
    number = 1,
    timingAlongCurve = 0,
  }) {
    super(
      x,
      y,
      radius,
      color,
      approchRadius,
      approchSpeed,
      velocity,
      (number = 1)
    );
    this.startPoints = startPoints;
    this.ctp1 = ctp1;
    this.ctp2 = ctp2;
    this.endPoints = endPoints;
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.color = color;
    this.approchRadius = approchRadius;
    this.approchSpeed = approchSpeed;
    this.velocity = velocity;
    this.number = number;
    this.timingAlongCurve = timingAlongCurve;
    this.ClipX = CERCLE_RADIUS * 2 - BORDER_WIDTH;
    this.ClipY = CERCLE_RADIUS * 2 - BORDER_WIDTH;
  }

  calculateBezierPoint(t, p0, p1, p2, p3) {
    const u = 1 - t;
    return (
      u * u * u * p0 + 3 * u * u * t * p1 + 3 * u * t * t * p2 + t * t * t * p3
    );
  }

  drawNumber() {
    if (this.number < 10) {
      const x = this.startPoints.x - CERCLE_RADIUS - FONT_SIZE / 4;
      const y = this.startPoints.y + FONT_SIZE / 2;
      c.fillStyle = "white";
      c.font = `${FONT_SIZE}px Arial`;
      c.fillText(this.number, x, y);
    } else {
      this.number = 1;
      COMBO = 1;
    }
  }

  drawMainCercle() {
    const x = this.calculateBezierPoint(
      this.timingAlongCurve,
      this.startPoints.x - CERCLE_RADIUS,
      this.ctp1.x - CERCLE_RADIUS,
      this.ctp2.x + CERCLE_RADIUS,
      this.endPoints.x + CERCLE_RADIUS
    );
    const y = this.calculateBezierPoint(
      this.timingAlongCurve,
      this.startPoints.y,
      this.ctp1.y + CERCLE_RADIUS,
      this.ctp2.y + CERCLE_RADIUS,
      this.endPoints.y
    );
    c.beginPath();
    c.fillStyle = this.color;
    c.arc(x, y, this.radius - BORDER_WIDTH, 0, Math.PI * 2);
    c.fill();
    this.timingAlongCurve +=
      APPROCH_SPEED / (this.endPoints.x - this.startPoints.x);
    if (this.timingAlongCurve > 1) this.timingAlongCurve = 0;
  }

  drawStartCercle() {
    c.strokeStyle = BORDER_COLOR;
    c.lineWidth = BORDER_WIDTH;
    c.beginPath();
    c.fillStyle = this.color;
    c.arc(
      this.startPoints.x - CERCLE_RADIUS + BORDER_WIDTH / 2,
      this.startPoints.y,
      this.radius,
      0,
      Math.PI * 2
    );
    c.fill();
    // c.beginPath();
    // c.fillStyle = this.color;
    // c.arc(
    //   this.startPoints.x - CERCLE_RADIUS + BORDER_WIDTH / 2,
    //   this.startPoints.y,
    //   this.radius,
    //   0,
    //   Math.PI * 2
    // );
    // c.fill();
    c.stroke();
  }

  drawArroundCercle() {
    c.strokeStyle = this.color;
    c.lineWidth = BORDER_WIDTH;
    c.save();
    c.beginPath();
    c.fillStyle = "transparent";
    c.arc(
      this.startPoints.x - CERCLE_RADIUS + BORDER_WIDTH / 2,
      this.startPoints.y,
      this.radius + this.approchRadius,
      0,
      Math.PI * 2,
      false
    );
    c.fill();
    c.restore();
    c.stroke();
  }

  drawInCurve() {
    c.beginPath();
    c.moveTo(this.startPoints.x, this.startPoints.y);
    c.bezierCurveTo(
      this.ctp1.x,
      this.ctp1.y,
      this.ctp2.x,
      this.ctp2.y,
      this.endPoints.x,
      this.endPoints.y
    );
    // ctx.bezierCurveTo(20, 100, 200, 100, 200, 20);
    c.stroke();
  }

  drawOutCurve() {
    c.beginPath();
    c.moveTo(this.startPoints.x - this.ClipX, this.startPoints.y);
    c.bezierCurveTo(
      this.ctp1.x - this.ClipX,
      this.ctp1.y + this.ClipY+20,
      this.ctp2.x + this.ClipX,
      this.ctp2.y + this.ClipY+20,
      this.endPoints.x + this.ClipX,
      this.endPoints.y
    );
    // ctx.bezierCurveTo(20, 100, 200, 100, 200, 20);
    c.stroke();
  }

  update() {
    if (c.globalAlpha < 1) {
      c.globalAlpha += (APPROCH_SPEED / APPROCH_RADIUS) * 1.6;
    }
    c.strokeStyle = BORDER_COLOR;
    c.lineWidth = BORDER_WIDTH;
    this.drawInCurve();
    this.drawOutCurve();
    if (this.radius + this.approchRadius - BORDER_WIDTH < this.radius) {
      this.drawMainCercle();
    } else {
      this.drawStartCercle();
    }
    this.drawArroundCercle();
    this.drawNumber();
  }
}
//! Init Slide Object
const x = canvas.width / 2;
const y = canvas.height / 2;
let slide = new Slide({
  startPoints: { x: 150, y: 200 },
  ctp1: { x: 150, y: 450 },
  ctp2: { x: 500, y: 450 },
  endPoints: { x: 500, y: 200 },
  x: x,
  y: y,
  radius: CERCLE_RADIUS,
  color: `hsl(${hsl}, 70%, 50%)`,
  approchRadius: APPROCH_RADIUS,
  approchSpeed: APPROCH_SPEED,
  velocity: { x: 5, y: 0 },
  number: COMBO,
});

//! Click Sound
function clickSound() {
  const Click_Sound = new Audio("./Assets/osu-hit-sound.mp3");
  Click_Sound.currentTime = 0;
  Click_Sound.volume = 1;
  Click_Sound.play();
}

//! Check Approch Cercle Position
function checkApprochCerclePosition(click = false) {
  if (slide.approchRadius > 0) {
    // console.log("Desincrement");
    slide.approchRadius -= slide.approchSpeed;
  }
}

//* Animate Function
function animate() {
  animationId = requestAnimationFrame(animate);
  c.fillStyle = CANVAS_BACKGROUND;
  c.fillRect(0, 0, canvas.width, canvas.height);
  slide.update();
  checkApprochCerclePosition();
  // cercle1.update();
  // cercle2.update();
}
animate();

// const canvas = document.querySelector("canvas");
// const ctx = canvas.getContext("2d");
// canvas.width = innerWidth;
// canvas.height = innerHeight;
// const controlPoint1 = { x: 100, y: 300 };
// const controlPoint2 = { x: 300, y: 100 };
// const endPoint = { x: 400, y: 300 };
// let t = 0;

// function drawBezierCurve() {
//   ctx.clearRect(0, 0, canvas.width, canvas.height);
//   ctx.fillStyle = "rgb(43, 43, 43)";
//   ctx.fillRect(0, 0, canvas.width, canvas.height);

//   // Draw the Bezier curve
//   ctx.beginPath();
//   ctx.moveTo(100, 300);
//   ctx.bezierCurveTo(
//     controlPoint1.x,
//     controlPoint1.y,
//     controlPoint2.x,
//     controlPoint2.y,
//     endPoint.x,
//     endPoint.y
//   );
//   ctx.stroke();

//   // Calculate the position of the arc along the Bezier curve
//   const x = calculateBezierPoint(
//     t,
//     100,
//     controlPoint1.x,
//     controlPoint2.x,
//     endPoint.x
//   );
//   const y = calculateBezierPoint(
//     t,
//     300,
//     controlPoint1.y,
//     controlPoint2.y,
//     endPoint.y
//   );

//   // Draw the arc at the calculated position
//   ctx.beginPath();
//   ctx.arc(x, y, 10, 0, 2 * Math.PI);
//   ctx.fillStyle = "blue";
//   ctx.fill();
//   ctx.closePath();

//   // Increment the parameter t for the next frame
//   t += 0.005;
//   if (t > 1) t = 0;

//   // Request the next animation frame
//   requestAnimationFrame(drawBezierCurve);
// }

// // Start the animation
// drawBezierCurve();

// function calculateBezierPoint(t, p0, p1, p2, p3) {
//   const u = 1 - t;
//   return (
//     u * u * u * p0 + 3 * u * u * t * p1 + 3 * u * t * t * p2 + t * t * t * p3
//   );
// }
