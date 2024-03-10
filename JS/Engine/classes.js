class Fighter {
  constructor({ position, velocity, color }) {
    this.position = position;
    this.velocity = velocity;
    this.height = 150;
    this.width = 50;
    this.radius = 20;
    this.resistance = { x: 0, y: 0 }; // 40 = this.radius
    this.color = color;
    this.health = 100;
  }

  draw() {
    //! Draw Arc
    c.beginPath();
    c.fillStyle = this.color;
    c.arc(this.position.x, this.position.y, this.radius, 0, Math.PI * 2, false);
    c.fill();
  }
  applyGravity() {
    this.velocity.y += gravity;
    this.velocity.y -= this.resistance.y * this.velocity.y; // Resistance

    this.position.x += this.velocity.x;
    this.position.y += this.velocity.y;

    if (this.position.y + this.radius >= canvas.height) {
      this.position.y = canvas.height - this.radius;
      this.velocity.y = -this.velocity.y; // Bounce back up
    }
  }

  applyResistance() {
    // Applying resistance on x-axis (for example)
    this.velocity.x -= this.resistance.x * this.velocity.x;
  }

  update() {
    this.applyGravity();
    this.applyResistance();
    this.draw();
  }
}

// class Fighter {
//   constructor({ position, velocity, color }) {
//     this.position = position;
//     this.velocity = velocity;
//     this.height = 150;
//     this.width = 50;
//     this.radius = 20;
//     this.resistance = { x: 0, y: 0 }; // 40 = this.radius
//     this.color = color;
//     this.health = 100;
//   }

//   draw() {
//     //! Draw Arc
//     c.beginPath();
//     c.fillStyle = this.color;
//     c.arc(this.position.x, this.position.y, this.radius, 0, Math.PI * 2, false);
//     c.fill();

//     //! Draw Rect
//     //   c.fillStyle = this.color;
//     // c.fillRect(this.position.x, this.position.y, this.width, this.height);
//   }

//   update() {
//     this.draw();
//     if (this.resistance.y !== 2.75 || this.resistance.y == 0) {
//       this.position.x += this.velocity.x;
//       this.position.y += this.velocity.y;

//       //! Arc gravity Bottom
//       if (this.position.y + this.radius + this.velocity.y >= canvas.height) {
//         this.velocity.y = 0;
//         this.position.y = canvas.height - this.radius;
//         this.velocity.y = -this.resistance.y;
//         // console.log("Resistance: ", this.resistance.y);
//       } else {
//         this.velocity.y += this.radius ;
//         this.resistance.y += Math.abs(this.velocity.y) / (this.radius * 20);
//         if (this.velocity.y < 0) {
//           // console.log("Velovity-Y: ", this.velocity.y);
//           this.resistance.y = this.resistance.y / 5;
//           // console.log("Gravity: ", this.resistance.y);
//         }
//       }
//       //! Arc gravity Left
//       //   if (this.position.x  + this.velocity.x <= 0) {
//       //     this.velocity.y = 0;
//       //     this.position.y = canvas.height - this.radius;
//       //     this.velocity.y = -this.resistance;
//       //     console.log("Resistance: ", this.resistance);
//       //   } else {
//       //     this.velocity.y += this.radius / 20;
//       //     this.resistance += ((this.radius / 40)+Math.abs(this.velocity.y/200));
//       //     if (this.velocity.y < 0) {
//       //       console.log("Velovity-Y: ", this.velocity.y);
//       //       this.resistance = this.resistance / 5;
//       //       console.log("Gravity: ", this.resistance);
//       //     }
//       // }
//     }

//     //! Rect gravity function
//     // if (this.position.y + this.height + this.velocity.y > canvas.height) {
//     //   this.velocity.y = 0;
//     //   this.position.y = canvas.height-this.height;
//     // } else {
//     //   this.velocity.y += gravity;
//     // }

//     //! Zone limit
//     // if (this.position.x < 0) {
//     //   this.position.x = 0;
//     // }
//     // if (this.position.x + this.width > canvas.width) {
//     //   this.position.x = canvas.width - this.width;
//     // }

//     //! Zone limit recursion
//     // if (this.position.x < -this.width) {
//     //   this.position.x = canvas.width - this.width;
//     // }
//     // if (this.position.x + this.width > canvas.width + this.width) {
//     //   this.position.x = 0;
//     // }
//   }

//   takeHit(getDamage, displacement) {
//     //! Take damage value from the ennemy
//     this.health -= getDamage;
//     this.position.x += displacement;
//   }
// }
