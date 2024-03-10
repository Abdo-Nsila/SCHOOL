const canvas = document.querySelector("canvas");
const c = canvas.getContext("2d");

//!---------------- SETTINGS ------------------
canvas.width = innerWidth;
canvas.height = innerHeight;
const CANVAS_BACKGROUND = "rgba(0,0,0,0.1)";

const SPEED_PLAYER = 25;
const SPEED_ENEMY = 15;
const SPEED_PROJECTILE = 4;
const CHECK_DEAD = false;
const DESTROY_ENEMY = true;
const RESPAWN_ENEMY_SPEED = 500;
const ENEMEY_DENSITY = 1;
const ENEMY_SIZE = 100;
const PROJECTILES_DENSITY = 10;
const SPEED_MOVE_SQUARE = 200;
//! --------------------------------------------

const scoreElement = document.querySelector("#score");
const startGameBtn = document.querySelector("#startGameEl");
const modalEl = document.querySelector("#modalEl");
const resultBoxEl = document.querySelector("#resultBox");
const resultEl = document.querySelector("#result");

// Initiale Player
const x = canvas.width / 2;
const y = canvas.height / 2;

var velocity = { x: 0, y: 0 };
var player = new Player(x, y, 15, "white", velocity);
var projectiles = [];
var enemies = [];
var particles = [];

function init() {
  player = new Player(x, y, 15, "white", velocity);
  projectiles = [];
  enemies = [];
  particles = [];
  score = 0;
  scoreElement.innerHTML = score;
  resultEl.innerHTML = score;
}

function spawnEnemies() {
  setInterval(() => {
    for (let index = 0; index < ENEMEY_DENSITY; index++) {
      const radius = Math.random() * (ENEMY_SIZE - 10) + 7;
      let x;
      let y;
      if (Math.random() < 0.5) {
        x = Math.random() < 0.5 ? 0 - radius : canvas.width + radius;
        y = Math.random() * canvas.height;
      } else {
        x = Math.random() * canvas.width;
        y = Math.random() < 0.5 ? 0 - radius : canvas.height + radius;
      }
      const color = `hsl(${Math.random() * 360}, 100%, 50%)`;
      // attack target (player)
      const angle = Math.atan2(player.y - y, player.x - x);
      const velocity = {
        x: Math.cos(angle) * SPEED_ENEMY,
        y: Math.sin(angle) * SPEED_ENEMY,
      };

      enemies.push(new Enemy(x, y, radius, color, velocity));
      // console.log(enemies);
    }
  }, RESPAWN_ENEMY_SPEED);
}
let framess = 0;
let animationId;
let score = 0;

if (framess % 60 === 0) {
  spawnEnemies();
}

const directions = {
  x: {
    precced: false,
    speed: 50,
  },
  y: {
    precced: true,
    speed: 50,
  },
};
function moveSquare() {
  console.log("x: ", directions.x.precced);
  console.log("y: ", directions.y.precced);
  if (directions.x.precced) {
    console.log("x");
    player.velocity.y = 0;
    player.velocity.x = directions.x.speed;
    directions.x.speed *= -1;
    directions.x.precced = false;
    directions.y.precced = true;
  } else if (directions.y.precced) {
    console.log("y");
    player.velocity.y = directions.y.speed;
    player.velocity.x = 0;
    directions.y.speed *= -1;
    directions.y.precced = false;
    directions.x.precced = true;
  }
}

// Animate Function
function animate() {
  framess++;
  animationId = requestAnimationFrame(animate);
  c.fillStyle = CANVAS_BACKGROUND;
  c.fillRect(0, 0, canvas.width, canvas.height);
  //! Move player
  player.update();

  particles.forEach((particle, indexPerticle) => {
    particle.alpha <= 0 ? particles.slice(indexPerticle, 1) : particle.update();
  });
  projectiles.forEach((projectile, projectileIndex) => {
    projectile.update();

    // Remove projectile from screen after out
    if (
      projectile.x + projectile.radius < 0 ||
      projectile.x - projectile.radius > canvas.width ||
      projectile.y + projectile.radius < 0 ||
      projectile.y - projectile.radius > canvas.height
    ) {
      setTimeout(() => {
        projectiles.splice(projectileIndex, 1);
      }, 0);
    }
  });

  // Check for collision
  enemies.forEach((enemy, enemyIndex) => {
    // Update enemy position for attack target (player)
    const angle = Math.atan2(player.y - enemy.y, player.x - enemy.x);
    const velocity = {
      x: Math.cos(angle) * SPEED_ENEMY,
      y: Math.sin(angle) * SPEED_ENEMY,
    };
    enemy.velocity = velocity;
    enemy.update();

    //! DESTROY ENEMY after collision
    if (DESTROY_ENEMY) {
      const distance = Math.hypot(player.x - enemy.x, player.y - enemy.y);

      if (distance - enemy.radius - player.radius < 1) {
        for (let i = 0; i < enemy.radius / 4; i++) {
          particles.push(
            new Particle(enemy.x, enemy.y, Math.random() * 3, enemy.color, {
              x: (Math.random() - 0.5) * (Math.random() * 6),
              y: (Math.random() - 0.5) * (Math.random() * 6),
            })
          );
        }

        if (enemy.radius - 10 > 5) {
          // Increase score
          score += 50;
          scoreElement.innerHTML = score;
          enemy.radius -= 10
          // enemy.radius -= 10;
          // gsap.to(enemy, {
          //   radius: enemy.radius - 10,
          // });
        } else {
          var sound = new Audio("./Assets/0110.MP3");
          sound.currentTime = 0;
          sound.play();
          // Increase score from screen
          score += 100;
          scoreElement.innerHTML = score;
          // Set Timeout for remove flash effect
          setTimeout(() => {
            enemies.splice(enemyIndex, 1);
          }, 0);
        }
      }
    }
    //! End Game
    else if (CHECK_DEAD) {
      const distance = Math.hypot(player.x - enemy.x, player.y - enemy.y);
      if (distance - enemy.radius - player.radius < 1) {
        cancelAnimationFrame(animationId);
        resultEl.innerHTML = score;
        startGameBtn.innerHTML = "Restart Game";
        resultBoxEl.style.display = "block";
        modalEl.style.display = "flex";
      }
    }
    projectiles.forEach((projectile, projectileIndex) => {
      const distance = Math.hypot(
        projectile.x - enemy.x,
        projectile.y - enemy.y
      );

      // When projectiles touch enemy
      if (distance - enemy.radius - projectile.radius < 1) {
        // create explosions
        //! for (let i = 0; i < enemy.radius * 2; i++) {
        for (let i = 0; i < enemy.radius / 2; i++) {
          particles.push(
            new Particle(
              projectile.x,
              projectile.y,
              Math.random() * 3,
              enemy.color,
              {
                x: (Math.random() - 0.5) * (Math.random() * 6),
                y: (Math.random() - 0.5) * (Math.random() * 6),
              }
            )
          );
        }
        if (enemy.radius - 10 > 5) {
          // Increase score
          score += 50;
          scoreElement.innerHTML = score;
          // enemy.radius -= 10;
          gsap.to(enemy, {
            radius: enemy.radius - 10,
          });
          setTimeout(() => {
            projectiles.splice(projectileIndex, 1);
          }, 0);
        } else {
          // Increase score from screen
          score += 100;
          scoreElement.innerHTML = score;
          // Set Timeout for remove flash effect
          setTimeout(() => {
            projectiles.splice(projectileIndex, 1);
            enemies.splice(enemyIndex, 1);
          }, 0);
        }
      }
    });
  });
}

window.addEventListener("resize", () => {
  canvas.width = innerWidth;
  canvas.height = innerHeight;
});

// window.addEventListener("mousemove", (e) => {
//   const angle = Math.atan2(e.clientY - player.y, e.clientX - player.x);
//   const velocity = {
//     x: Math.cos(angle) * SPEED_PROJECTILE,
//     y: Math.sin(angle) * SPEED_PROJECTILE,
//   };

//   for (let index = 0; index < PROJECTILES_DENSITY; index++) {
//   projectiles.push(new Projectile(player.x, player.y, 5, "white", velocity));
//   }
// });

startGameBtn.addEventListener("click", () => {
  init();
  animate();
  modalEl.style.display = "none";
  //! Auto Play Square
  // setInterval(() => moveSquare(), SPEED_MOVE_SQUARE);
});

//! Move Witn Keys
window.addEventListener("keydown", (e) => {
  if (e.key === "z") {
    player.velocity = { x: 0, y: -SPEED_PLAYER };
  }
  if (e.key === "s") {
    player.velocity = { x: 0, y: SPEED_PLAYER };
  }
  if (e.key === "q") {
    player.velocity = { x: -SPEED_PLAYER, y: 0 };
  }
  if (e.key === "d") {
    player.velocity = { x: SPEED_PLAYER, y: 0 };
  }
  // switch (e.key) {
  //   case "z":
  //     player.velocity = { x: 0, y: -SPEED_PLAYER };
  //     break;
  //   case "s":
  //     player.velocity = { x: 0, y: SPEED_PLAYER };
  //     break;
  //   case "q":
  //     player.velocity = { x: -SPEED_PLAYER, y: 0 };
  //     break;
  //   case "d":
  //     player.velocity = { x: SPEED_PLAYER, y: 0 };
  //     break;
  // }
});

function move_with_mouse(event) {
  const distance = Math.hypot(
    player.x - event.clientX,
    player.y - event.clientY
  );
  if (distance > 120) {
    const angle = Math.atan2(
      event.clientY - player.y,
      event.clientX - player.x
    );
    const velocity = {
      x: Math.cos(angle) * SPEED_PLAYER,
      y: Math.sin(angle) * SPEED_PLAYER,
    };
    player.velocity = velocity;
  }
}

window.addEventListener("mousemove", handler, false);
// window.addEventListener("mousedown", handler, false);

function handler(event) {
  move_with_mouse(event);
}
