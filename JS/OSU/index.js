const canvas = document.querySelector("canvas");
const c = canvas.getContext("2d");
const cursor = document.querySelector(".cursor");
//!---------------- SETTINGS ------------------
// const DevicePixelRatio = window.devicePixelRatio || 1;
const bg_audio = new Audio('./Assets/y2mate.bz - matteo-panama-lyrics-tiktok-remix.mp3')
bg_audio.play()
const DevicePixelRatio = 1;
canvas.width = innerWidth;
canvas.height = innerHeight;
const CURSEUR = {
  MouseX: 0,
  MouseY: 0,
  sensitivity: 1,
  size: 20,
  DISTANCE: 0,
};
let COMBO = 0;
let hsl = Math.floor(Math.random() * (200 - 0 + 1) + 0);
let score = 0;
const CANVAS_BACKGROUND = "rgb(43, 43, 43)";
const CERCLE_RADIUS = 60;
const APPROCH_RADIUS = CERCLE_RADIUS * 3;
const APPROCH_SPEED = 5;
const BORDER_WIDTH = 6;
const BORDER_COLOR = "white";
const FONT_SIZE = CERCLE_RADIUS - CERCLE_RADIUS / 5;
const Game_Confirm = new Audio("./Assets/match-confirm.ogg");
// return Math.floor(Math.random() * (max - min + 1) + min);
// const Click_Sound = new Audio("./Assets/soft-hitclap.wav");
// Click_Sound.volume = 1;
// Click_Sound.load();
// cursor.style.height = CURSEUR.size + "px";
// cursor.style.width = CURSEUR.size + "px";

//!--------------- Cercle Class -----------------
class Cercle {
  constructor({
    x,
    y,
    oldX = 0,
    oldY = 0,
    radius,
    color,
    approchRadius,
    approchSpeed,
    velocity,
    number = 1,
  }) {
    this.x = x;
    this.y = y;
    this.oldX = oldX;
    this.oldY = oldY;
    this.radius = radius;
    this.color = color;
    this.approchRadius = approchRadius;
    this.approchSpeed = approchSpeed;
    this.velocity = velocity;
    this.number = number;
  }

  drawNumber() {
    if (this.number < 10) {
      const x = this.x - FONT_SIZE / 4;
      const y = this.y + FONT_SIZE / 2;
      c.fillStyle = "white";
      c.font = `${FONT_SIZE}px Arial`;
      c.fillText(this.number, x, y);
    } else {
      this.number = 1;
      COMBO = 1;
    }
  }

  drawMainCercle() {
    c.strokeStyle = BORDER_COLOR;
    c.lineWidth = BORDER_WIDTH;
    c.save();
    c.beginPath();
    c.fillStyle = this.color;
    c.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
    c.fill();
    c.restore();
    c.stroke();
  }

  drawArroundCercle() {
    c.strokeStyle = this.color;
    c.lineWidth = BORDER_WIDTH;
    c.save();
    c.beginPath();
    c.fillStyle = "transparent";
    c.arc(
      this.x,
      this.y,
      this.radius + this.approchRadius,
      0,
      Math.PI * 2,
      false
    );
    c.fill();
    c.restore();
    c.stroke();
  }

  update() {
    if (c.globalAlpha < 1) {
      c.globalAlpha += (APPROCH_SPEED / APPROCH_RADIUS) * 2;
      // //* Start a new Path
      // c.strokeStyle = "white";
      // c.lineWidth = 2;
      // c.beginPath();
      // c.moveTo(this.oldX, this.oldY);
      // c.lineTo(this.x, this.y);
      // //* Draw the Path
      // c.stroke();
    }
    this.drawMainCercle();
    this.drawArroundCercle();
    this.drawNumber();
    // this.x += this.velocity.x;
    // this.y += this.velocity.y;
  }
}
//!----------------------------- ResultClap Class ----------------------------
class ResultClap {
  constructor({ x, y, color, img, timeLife = 1 }) {
    this.x = x;
    this.y = y;
    this.color = color;
    this.img = img;
    this.timeLife = timeLife;
  }

  draw() {
    this.timeLife -= 0.04;

    const image = new Image(85, 85); // Using optional size for image
    image.src = this.img;
    // c.globalAlpha = 0.4;
    c.drawImage(
      image,
      this.x - image.width / 2,
      this.y - image.height / 2,
      image.width,
      image.height
    );
    // c.save();
    // c.beginPath();
    // c.fillStyle = this.color;
    // c.arc(this.x, this.y, 30, 0, Math.PI * 2, false);
    // c.fill();
    // c.restore();
  }
  update() {
    this.draw();
  }
}

let cercles = [];
let resultsClaps = [];

const x = canvas.width / 2;
const y = canvas.height / 2;
RespawnCercle(x, y);

function pad(num, size) {
  num = num.toString();
  while (num.length < size) num = "0" + num;
  return num;
}

//! Respawn Cercle Funcion
function RespawnCercle(oldX, oldY) {
  c.globalAlpha = 0;
  hsl += 10;
  COMBO += 1;
  const newX = Math.abs(
    Math.random() * (canvas.width - APPROCH_RADIUS - APPROCH_RADIUS) +
      APPROCH_RADIUS
  );
  const newY = Math.abs(
    Math.random() * (canvas.height - APPROCH_RADIUS - APPROCH_RADIUS) +
      APPROCH_RADIUS
  );

  cercle = new Cercle({
    x: newX,
    y: newY,
    oldX: oldX,
    oldY: oldY,
    radius: CERCLE_RADIUS,
    color: `hsl(${hsl}, 70%, 50%)`,
    approchRadius: APPROCH_RADIUS,
    approchSpeed: APPROCH_SPEED,
    velocity: { x: 5, y: 0 },
    number: COMBO,
  });

  //! Respawn with animation
  // cercle.radius = CERCLE_RADIUS;
  // cercle.color = `hsl(${hsl}, 70%, 50%)`;
  // cercle.approchRadius = APPROCH_RADIUS;
  // cercle.approchSpeed = APPROCH_SPEED;
  // cercle.velocity = { x: 5, y: 0 };
  // cercle.number = COMBO;
  // gsap.to(cercle, { opacity: 1, duration: 3 });
  // gsap.to(cercle, {
  //   x: newX,
  //   y: newY,
  //   duration: 1,
  // });
}

//! Click Sound
function clickSound() {
  const Click_Sound = new Audio("./Assets/osu-hit-sound.mp3");
  Click_Sound.currentTime = 0;
  Click_Sound.volume = 1;
  Click_Sound.play();
}

//! Check Approch Cercle Position
function checkApprochCerclePosition(click = false) {
  const PRECISION =
    ((cercle.radius + cercle.approchRadius) * 100) / cercle.radius;
  let currentAccuracy = 0;
  const PrevAccuuracy = Number(
    document.querySelector("#accuracy").innerHTML.split("%")[0]
  );
  if (click && cercle.radius + cercle.approchRadius >= cercle.radius) {
    console.log("Click");
    if (PRECISION >= 100 && PRECISION < 110) {
      // console.log("Accuracy 100%", PRECISION);
      score += 300;
      currentAccuracy = (100 + PrevAccuuracy) / 2;
    } else if (PRECISION >= 110 && PRECISION < 140) {
      resultsClaps.push(
        new ResultClap({
          x: cercle.x,
          y: cercle.y,
          color: "#5cff5c",
          img: "./Assets/hit300@2x.png",
        })
      );
      console.log("Accuracy 90%", PRECISION);
      score += 250;
      currentAccuracy = (90 + PrevAccuuracy) / 2;
    } else if (PRECISION >= 140 && PRECISION < 170) {
      resultsClaps.push(
        new ResultClap({
          x: cercle.x,
          y: cercle.y,
          color: "#feb224",
          img: "./Assets/hit100@2x.png",
        })
      );
      // console.log("Accuracy 60%", PRECISION);
      score += 100;
      currentAccuracy = (60 + PrevAccuuracy) / 2;
    } else if (PRECISION >= 170) {
      resultsClaps.push(
        new ResultClap({
          x: cercle.x,
          y: cercle.y,
          color: "#8b0000",
          img: "./Assets/hit50@2x.png",
        })
      );
      // console.log("Accuracy 30%", PRECISION);
      score += 40;
      currentAccuracy = (30 + PrevAccuuracy) / 2;
    }
    //! Set Score and Accuracy
    document.querySelector("#score").innerHTML = pad(score, 8);
    document.querySelector("#accuracy").innerHTML =
      currentAccuracy.toString().slice(0, 5) + "%";
    //! Sound Effect
    clickSound();
    RespawnCercle(cercle.x, cercle.y);
  } else if (
    cercle.radius + cercle.approchRadius - BORDER_WIDTH <=
    cercle.radius - BORDER_WIDTH
  ) {
    // console.log("Lose: ");
    // clickSound();
    resultsClaps.push(
      new ResultClap({
        x: cercle.x,
        y: cercle.y,
        color: "red",
        img: "./Assets/close_red.png",
      })
    );
    document.querySelector("#accuracy").innerHTML =
      PrevAccuuracy.toString().slice(0, 5) / 2 + "%";
    RespawnCercle(cercle.x, cercle.y);
  }
  if (cercle.approchRadius + BORDER_WIDTH > 0) {
    // console.log("Desincrement");
    cercle.approchRadius -= cercle.approchSpeed;
  }
}

//* Animate Function
function animate() {
  animationId = requestAnimationFrame(animate);
  // c.clearRect(0, 0, canvas.width, canvas.height);
  c.fillStyle = CANVAS_BACKGROUND;
  c.fillRect(0, 0, canvas.width, canvas.height);
  //! Draw Cercles
  cercle.update();
  //! Draw Results Clap
  resultsClaps.forEach((element, index) => {
    if (element.timeLife <= 0) {
      // console.log(resultsClaps);
      resultsClaps.splice(index, 1);
    }
    element.update();
  });
  checkApprochCerclePosition();
}

//!--------------------- Event Listener -----------------------
window.addEventListener("mousemove", (e) => {
  const rect = canvas.getBoundingClientRect(); // Get the canvas's position relative to the viewport
  CURSEUR.MouseX = e.clientX - rect.left; // Calculate the mouse X coordinate relative to the canvas
  CURSEUR.MouseY = e.clientY - rect.top; // Calculate the mouse Y coordinate relative to the canvas
  cursor.style.left = e.pageX + "px";
  cursor.style.top = e.pageY + "px";
  CURSEUR.DISTANCE = Math.hypot(e.clientX - cercle.x, e.clientY - cercle.y);
});

const Keys = {
  s: {
    precced: false,
  },
  q: {
    precced: false,
  },
};
window.addEventListener("keydown", (e) => {
  if (
    CURSEUR.DISTANCE < CERCLE_RADIUS &&
    (e.key === "s" || e.key === "q") &&
    Keys[e.key].precced === false
  ) {
    Keys[e.key].precced = true;
    checkApprochCerclePosition(true);
  }
});

window.addEventListener("keyup", (e) => {
  if (e.key === "s" || e.key === "q") {
    Keys[e.key].precced = false;
  }
});
// Game_Confirm.addEventListener("ended", function () {
//   console.log("Audio has finished playing");
//   animate();
// });

// Game_Confirm.play();
animate();

//! ------------------------------- Comments ------------------------------
// c.shadowColor = "rgba(255, 255, 255";
// c.shadowBlur = 60;
// c.strokeRect(this.x, this.y, this.radius, this.radius);
// c.strokeStyle = "white";
// c.lineWidth = 5;
// c.roundRect(30,30,this.radius,this.radius,60)
