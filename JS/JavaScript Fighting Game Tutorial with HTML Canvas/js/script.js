const canvas = document.querySelector("#canvas");
const c = canvas.getContext("2d");

canvas.width = 1024;
canvas.height = 576;

c.fillRect(0, 0, canvas.width, canvas.height);

const gravity = 0.7;

const player_sword1 = new Audio('/Sound Effects/clean-fast-swooshaiff-14784.mp3')
const enemy_sword1 = new Audio('/Sound Effects/clean-fast-swooshaiff-14784.mp3')
const sword2 = new Audio('/Sound Effects/shield-block-shortsword-143940.mp3')

const background = new Sprite({
  position: { x: 0, y: 0 },
  imageSrc: "./Assets/background.png",
});
const shop = new Sprite({
  position: { x: 600, y: 128 },
  imageSrc: "./Assets/shop.png",
  scale: 2.75,
  framesMax: 6,
});

const player = new Fighter({
  position: { x: 50, y: 0 },
  velocity: { x: 0, y: -5 },
  color: "blue",
  offset: { x: 0, y: 0 },
  damage: 5,
  imageSrc: "./Assets/samuraiMack/Idle.png",
  framesMax: 8,
  scale: 2.5,
  offset: { x: 215, y: 157 },
  sprites: {
    idle: {
      imageSrc: "./Assets/samuraiMack/Idle.png",
      framesMax: 8,
    },
    run: {
      imageSrc: "./Assets/samuraiMack/Run.png",
      framesMax: 8,
    },
    jump: {
      imageSrc: "./Assets/samuraiMack/Jump.png",
      framesMax: 2,
    },
    fall: {
      imageSrc: "./Assets/samuraiMack/Fall.png",
      framesMax: 2,
    },
    attack1: {
      imageSrc: "./Assets/samuraiMack/Attack1.png",
      framesMax: 6,
    },
    attack2: {
      imageSrc: "./Assets/samuraiMack/Attack2.png",
      framesMax: 6,
    },
    takeHit: {
      imageSrc: "./Assets/samuraiMack/Take Hit - white silhouette.png",
      framesMax: 4,
    },
    death: {
      imageSrc: "./Assets/samuraiMack/Death.png",
      framesMax: 6,
    },
  },
  attackBox: {
    offset: { x: 50, y: 20 },
    width: 170,
    height: 130,
    // color: '#0f0',
  },
});
// console.log(player);


//! Old Enemy
const enemy = new Fighter({
  position: { x: 900, y: 0 },
  velocity: { x: 0, y: -5 },
  color: "red",
  offset: { x: -50, y: 0 },
  damage: 2,
  imageSrc: "./Assets/kenji/Idle.png",
  framesMax: 4,
  scale: 2.5,
  offset: { x: 215, y: 170 },
  sprites: {
    idle: {
      imageSrc: "./Assets/kenji/Idle.png",
      framesMax: 4,
    },
    run: {
      imageSrc: "./Assets/kenji/Run.png",
      framesMax: 8,
    },
    jump: {
      imageSrc: "./Assets/kenji/Jump.png",
      framesMax: 2,
    },
    fall: {
      imageSrc: "./Assets/kenji/Fall.png",
      framesMax: 2,
    },
    attack1: {
      imageSrc: "./Assets/kenji/Attack1.png",
      framesMax: 4,
    },
    attack2: {
      imageSrc: "./Assets/kenji/Attack2.png",
      framesMax: 4,
    },
    takeHit: {
      imageSrc: "./Assets//kenji/Take hit.png",
      framesMax: 3,
    },
    death: {
      imageSrc: "./Assets//kenji/Death.png",
      framesMax: 7,
    },
  },
  attackBox: {
    offset: { x: -150, y: 20 },
    width: 170,
    height: 130,
    // color: 'transparent',
  },
});
// console.log(enemy);

const keys = {
  q: {
    pressed: false,
  },
  d: {
    pressed: false,
  },
  ArrowLeft: {
    pressed: false,
  },
  ArrowRight: {
    pressed: false,
  },
};

decreaseTimer();

function animate() {
  window.requestAnimationFrame(animate);
  c.fillStyle = "#000";
  c.fillRect(0, 0, canvas.width, canvas.height);
  background.update();
  shop.update();
  // c.fillStyle = "rgba(255,255,255,0.1)";
  // c.fillRect(0, 0, canvas.width, canvas.height);
  player.update();
  enemy.update();

  // End game based on health
  if (enemy.health <= 0 || player.health <= 0) {
    determineWinner({ player, enemy, timerId });
  }

  //   Player mouvement
  player.velocity.x = 0;
  if (keys.q.pressed && player.lastKey === "q") {
    player.velocity.x = -5;
    player.switchSprite("run");
  } else if (keys.d.pressed && player.lastKey === "d") {
    player.velocity.x = 5;
    player.switchSprite("run");
  } else {
    player.switchSprite("idle");
  }

  if (player.velocity.y < 0) {
    player.switchSprite("jump");
  } else if (player.velocity.y > 0) {
    player.switchSprite("fall");
  }

  //   Enemy mouvement
  enemy.velocity.x = 0;
  if (keys.ArrowLeft.pressed && enemy.lastKey === "ArrowLeft") {
    enemy.velocity.x = -5;
    enemy.switchSprite("run");
  } else if (keys.ArrowRight.pressed && enemy.lastKey === "ArrowRight") {
    enemy.velocity.x = 5;
    enemy.switchSprite("run");
  } else {
    enemy.switchSprite("idle");
  }

  if (enemy.velocity.y < 0) {
    enemy.switchSprite("jump");
  } else if (enemy.velocity.y > 0) {
    enemy.switchSprite("fall");
  }

  // detect for collision and enemy get hit
  if (
    rectangularCollision({ rectangle1: player, rectangle2: enemy }) &&
    player.isAttacking &&
    player.framesCurrent === 4
  ) {
    enemy.takeHit(player.damage, displacement=30);
    player.isAttacking = false;
    document.querySelector("#enemyHealth").style.width = `${enemy.health}%`;
    gsap.to("#enemyHealth", {
      width: `${enemy.health}%`,
    });
    console.log("Player attaking");
  }
  // Fix attack and pushing bug for player
  if (player.isAttacking && player.framesCurrent === 4) {
    player.isAttacking = false;
  }

  // this is where our player gets hit
  if (
    rectangularCollision({ rectangle1: enemy, rectangle2: player }) &&
    enemy.isAttacking &&
    enemy.framesCurrent === 2
  ) {
    player.takeHit(enemy.damage, displacement=-20);
    enemy.isAttacking = false;
    document.querySelector("#playerHealth").style.width = `${player.health}%`;
    gsap.to("#playerHealth", {
      width: `${player.health}%`,
    });
    console.log("Enemy attacking");
  }

  // Fix attack and pushing bug for enemy
  if (enemy.isAttacking && enemy.framesCurrent === 2) {
    enemy.isAttacking = false;
  }
}
animate();

window.addEventListener("keydown", (event) => {
  console.log(event)

  if (!player.death) {
    switch (event.key.toLowerCase()) {
      case "d":
        keys.d.pressed = true;
        player.lastKey = "d";
        break;
      case "q":
        keys.q.pressed = true;
        player.lastKey = "q";
        break;
      case " ":
        //! Jump & Down & Jump & Down ...
        if (player.position.y === 330) {
          player.velocity.y = -20;
        }
        break;
      case "t":
        player.attack("attack1");
        player_sword1.currentTime = 0
        player_sword1.volume = 0.1
        player_sword1.play()
        break;
        //! Adding Attack 2
        case "y":
          player.attack("attack2");
        break;
    }
  }

  if (!enemy.death) {
    switch (event.key) {
      //   Enemy
      case "ArrowRight":
        keys.ArrowRight.pressed = true;
        enemy.lastKey = "ArrowRight";
        break;
      case "ArrowLeft":
        keys.ArrowLeft.pressed = true;
        enemy.lastKey = "ArrowLeft";
        break;
      case "Shift":
        //! Jump & Down & Jump & Down ...
        if (enemy.position.y === 330) {
          enemy.velocity.y = -20;
        }
        break;
      case "1":
        enemy.attack("attack1");
        enemy_sword1.currentTime = 0
        enemy_sword1.volume = 0.1
        enemy_sword1.play()
        break;
      //! Adding Attack 2
      case "2":
        enemy.attack("attack2");
        break;
    }
  }
});

window.addEventListener("keyup", (event) => {
  switch (event.key.toLowerCase()) {
    case "d":
      keys.d.pressed = false;
      break;
    case "q":
      keys.q.pressed = false;
      break;
  }

  //   Enemy
  switch (event.key) {
    case "ArrowRight":
      keys.ArrowRight.pressed = false;
      break;
    case "ArrowLeft":
      keys.ArrowLeft.pressed = false;
      break;
  }
});

//! Audio Background
// window.addEventListener("DOMContentLoaded", (event) => {
//   const audio = document.querySelector("audio");
//   audio.volume = 0.05;
//   audio.play();
// });
