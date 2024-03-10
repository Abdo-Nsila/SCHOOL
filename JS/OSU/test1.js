const canvas = document.querySelector("canvas");
const ctx = canvas.getContext("2d");
canvas.width = innerWidth;
canvas.height = innerHeight;
ctx.fillStyle = "rgb(43, 43, 43)";
ctx.fillRect(0, 0, canvas.width, canvas.height);
const pathWidth = 2;
const limitColor = "white";

// // Slider properties
// const startCircleRadius = 60;
// const endCircleRadius = startCircleRadius;
// const pathWidth = 4;
// const pathColor = "blue";
// const limitWidth = 20; // Width of the track limits
// const limitColor = "white"; // Color of the track limits (semi-transparent blue)

// // // Coordinates for the start and end circles
// // const startX = 150;
// // const startY = 200;
// // const endX = 500;
// // const endY = 200;
// // // Control points for the Bezier curve
// // const controlPoint1X = 150;
// // const controlPoint1Y = 450;
// // const controlPoint2X = 500;
// // const controlPoint2Y = 450;
// // Coordinates for the start and end circles
// const startX = 150;
// const startY = 200;
// const endX = 600;
// const endY = 200;

// // Control points for the Bezier curve
// const controlPoint1X = 250;
// const controlPoint1Y = 100;
// const controlPoint2X = 450;
// const controlPoint2Y = 300;

// // Animation variables
// let t = 0;
// const animationSpeed = 0.005;

// function draw() {
//   ctx.clearRect(0, 0, canvas.width, canvas.height);
//   ctx.fillStyle = "rgb(43, 43, 43)";
//   ctx.fillRect(0, 0, canvas.width, canvas.height);

//   // Draw track limits (parallel lines)
//   const angle = Math.atan2(controlPoint2Y - startY, controlPoint2X - startX); // Angle of the Bezier curve
//   const dx = Math.sin(angle) + endCircleRadius / 1.5;
//   const dy = Math.cos(angle) + endCircleRadius / 1.5;
//   //   const dx = Math.sin(angle) * limitWidth;
//   //   const dy = Math.cos(angle) * limitWidth;

//     // Draw left limit
//     ctx.beginPath();
//     ctx.moveTo(startX - endCircleRadius + dx, startY - dy);
//     ctx.bezierCurveTo(
//       controlPoint1X + dx,
//       controlPoint1Y - dy,
//       controlPoint2X + dx,
//       controlPoint2Y - dy,
//       endX - endCircleRadius + dx,
//       endY - dy
//     );
//     ctx.lineWidth = pathWidth;
//     ctx.strokeStyle = limitColor;
//     ctx.stroke();

//     // Draw right limit
//     ctx.beginPath();
//     ctx.moveTo(startX + endCircleRadius - dx, startY + dy);
//     ctx.bezierCurveTo(
//       controlPoint1X - dx,
//       controlPoint1Y + dy,
//       controlPoint2X - dx,
//       controlPoint2Y + dy,
//       endX + endCircleRadius - dx,
//       endY + dy
//     );
//     ctx.lineWidth = pathWidth;
//     ctx.strokeStyle = limitColor;
//     ctx.stroke();

//   // Draw slider path (Bezier curve)
//   ctx.beginPath();
//   ctx.moveTo(startX + startCircleRadius, startY);
//   ctx.bezierCurveTo(
//     controlPoint1X,
//     controlPoint1Y,
//     controlPoint2X,
//     controlPoint2Y,
//     endX - endCircleRadius,
//     endY
//   );
//   ctx.lineWidth = pathWidth;
//   ctx.strokeStyle = pathColor;
//   ctx.stroke();

//   // Draw start circle
//   ctx.beginPath();
//   ctx.arc(startX, startY, endCircleRadius, 0, Math.PI * 2);
//   ctx.fillStyle = "red";
//   ctx.fill();

//   // Draw end circle
//   ctx.beginPath();
//   ctx.arc(endX, endY, endCircleRadius, 0, Math.PI * 2);
//   ctx.fillStyle = "red";
//   ctx.fill();

//   // Calculate current position of the cursor along the curve
//   const x = bezierCurveX(t, startX, controlPoint1X, controlPoint2X, endX);
//   const y = bezierCurveY(t, startY, controlPoint1Y, controlPoint2Y, endY);

//   // Draw cursor at current position
//   ctx.beginPath();
//   ctx.arc(x, y, dx, 0, Math.PI * 2); // Cursor size
//   ctx.fillStyle = "green";
//   ctx.fill();

//   // Increment parameter t for animation
//   t += animationSpeed;
//   if (t > 1) {
//     t = 0; // Reset animation when t exceeds 1
//   }

//   // Request next frame of animation
//   requestAnimationFrame(draw);
// }

// // Start the animation
// draw();

// // Helper functions to calculate points along Bezier curve
// function bezierCurveX(t, x0, x1, x2, x3) {
//   return (
//     (1 - t) ** 3 * x0 +
//     3 * (1 - t) ** 2 * t * x1 +
//     3 * (1 - t) * t ** 2 * x2 +
//     t ** 3 * x3
//   );
// }

// function bezierCurveY(t, y0, y1, y2, y3) {
//   return (
//     (1 - t) ** 3 * y0 +
//     3 * (1 - t) ** 2 * t * y1 +
//     3 * (1 - t) * t ** 2 * y2 +
//     t ** 3 * y3
//   );
// }

// const startPointX = parseInt(document.getElementById("startPointX").value);
// const startPointY = parseInt(document.getElementById("startPointY").value);
// const endPointX = parseInt(document.getElementById("endPointX").value);
// const endPointY = parseInt(document.getElementById("endPointY").value);
// const controlPoint1X = parseInt(
//   document.getElementById("controlPoint1X").value
// );
// const controlPoint1Y = parseInt(
//   document.getElementById("controlPoint1Y").value
// );

// Define semi-circle parameters for up slider
const startX = 150;
const startY = 300;
const endX = 250;
const endY = startY;
const controlPointX = (startX + endX) / 2;
const controlPointY = (endX-startX); // Adjust this value to control the height of the curve

// // Define semi-circle parameters for down slider
// const startX = 150;
// const startY = 300;
// const endX = 350;
// const endY = 300;
// const controlPointX = (startX + endX) / 2;
// const controlPointY = startY - startX; // Adjust this value to control the height of the curve

// Define circle parameters
const circleRadius = 20;
let circleX = startX;
let circleY = startY;
let t = 0; // Parameter for moving the circle along the curve

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "rgb(43, 43, 43)";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Draw semi-circle curve
  ctx.lineWidth = 1;
  ctx.strokeStyle = "yellow";
  ctx.beginPath();
  ctx.moveTo(startX, startY);
  ctx.bezierCurveTo(startX, startY, controlPointX, controlPointY, endX, endY);
  ctx.stroke();

  // Calculate current position of the circle along the semi-circle
  const { x, y } = bezierCurvePoint(
    startX,
    startY,
    controlPointX,
    controlPointY,
    endX,
    endY,
    t
  );
  circleX = x;
  circleY = y;

  // Draw circle at current positionctx.lineWidth = pathWidth;
  ctx.lineWidth = pathWidth * 4;
  ctx.strokeStyle = limitColor;
  ctx.beginPath();
  ctx.arc(circleX, circleY, circleRadius, 0, Math.PI * 2);
  ctx.fillStyle = "transparent";
  ctx.fill();
  ctx.stroke();

  //! Limits for Up slider
  // Draw UP limit
  ctx.lineWidth = pathWidth;
  ctx.strokeStyle = limitColor;
  ctx.beginPath();
  ctx.moveTo(startX + circleRadius / 2, startY - circleRadius);
  ctx.bezierCurveTo(
    startX + circleRadius / 2,
    startY - circleRadius,
    controlPointX,
    controlPointY - circleRadius,
    endX - circleRadius / 2,
    endY - circleRadius
  );
  ctx.stroke();

  // Draw Down limit
  ctx.lineWidth = pathWidth;
  ctx.strokeStyle = limitColor;
  ctx.beginPath();
  // ctx.moveTo(startX + circleRadius/2, startY + circleRadius);
  ctx.moveTo(startX - circleRadius / 2, startY + circleRadius);
  ctx.bezierCurveTo(
    startX - circleRadius / 2,
    startY + circleRadius,
    controlPointX,
    controlPointY + circleRadius,
    endX + circleRadius / 2,
    endY + circleRadius
  );
  ctx.stroke();

  //! Limits for Down slider
  // // Draw UP limit
  // ctx.lineWidth = pathWidth;
  // ctx.strokeStyle = limitColor;
  // ctx.beginPath();
  // ctx.moveTo(startX - circleRadius/2, startY - circleRadius);
  // ctx.bezierCurveTo(
  //   startX - circleRadius/2,
  //   startY - circleRadius,
  //   controlPointX,
  //   controlPointY - circleRadius,
  //   endX + circleRadius/2,
  //   endY - circleRadius
  // );
  // ctx.stroke();

  // // Draw Down limit
  // ctx.lineWidth = pathWidth;
  // ctx.strokeStyle = limitColor;
  // ctx.beginPath();
  // // ctx.moveTo(startX + circleRadius/2, startY + circleRadius);
  // ctx.moveTo(startX + circleRadius/2, startY + circleRadius);
  // ctx.bezierCurveTo(
  //   startX+circleRadius/2,
  //   startY + circleRadius,
  //   controlPointX,
  //   controlPointY + circleRadius,
  //   endX-circleRadius/2,
  //   endY + circleRadius
  // );
  // ctx.stroke();

  // Draw start circle
  ctx.beginPath();
  ctx.arc(startX, startY, circleRadius * 1.5, 0, Math.PI * 2);
  ctx.fillStyle = "green";
  ctx.fill();

  // Draw end circle
  ctx.beginPath();
  ctx.arc(endX, endY, circleRadius * 1.5, 0, Math.PI * 2);
  ctx.fillStyle = "blue";
  ctx.fill();

  // Increment parameter t for animation
  t += 0.005;
  if (t > 1) {
    t = 0; // Reset animation when t exceeds 1
  }

  // Request next frame of animation
  requestAnimationFrame(draw);
}

// Start the animation
draw();

// Helper function to calculate point on Bezier curve
function bezierCurvePoint(x0, y0, x1, y1, x2, y2, t) {
  const invT = 1 - t;
  const invT2 = invT * invT;
  const invT3 = invT2 * invT;
  const t2 = t * t;
  const t3 = t2 * t;

  const x = x0 * invT3 + 3 * x1 * t * invT2 + 3 * x2 * t2 * invT + x2 * t3;
  const y = y0 * invT3 + 3 * y1 * t * invT2 + 3 * y2 * t2 * invT + y2 * t3;

  return { x, y };
}
